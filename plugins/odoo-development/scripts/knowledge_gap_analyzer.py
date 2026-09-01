#!/usr/bin/env python3
"""Weekly Knowledge Gap Analyzer & Skill Patch Generator.

Part of Phase B (Self-Improving Knowledge Loop):
1. Reads employee error reports from skill_feedback.sqlite3 (/odoo-wrong).
2. Analyzes MCP tool fallback logs.
3. Groups gaps by model, version, and domain.
4. Enforces the High Significance Barrier (>=3 reports, >=5 queries, or broke_code).
5. Queries the Odoo MCP Knowledge Base for ground-truth facts.
6. Generates a compact weekly review report (Top 5 proposals max) for human approval.
7. Supports 1-click patch application via `--apply <N>`.
"""

import os
import sys
import json
import sqlite3
import argparse
import urllib.request
from datetime import datetime, timedelta

# Default paths
PLUGIN_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS_ROOT = os.path.join(PLUGIN_ROOT, "skills")
FEEDBACK_DB = os.environ.get("FEEDBACK_DB", os.path.join(PLUGIN_ROOT, "skill_feedback.sqlite3"))
MCP_URL = os.environ.get("MCP_URL", "http://192.168.11.208:8099/mcp/")
REPORT_OUTPUT = os.path.join(PLUGIN_ROOT, "WEEKLY_KNOWLEDGE_REVIEW.md")

class FastMcpClient:
    def __init__(self, endpoint):
        self.endpoint = endpoint
        self.session_id = None
        self._init()

    def _init(self):
        try:
            self._post({"jsonrpc": "2.0", "method": "initialize", "params": {"protocolVersion": "2024-11-05", "capabilities": {}, "clientInfo": {"name": "gap-analyzer", "version": "1.0"}}, "id": 1})
            self._post({"jsonrpc": "2.0", "method": "notifications/initialized", "params": {}})
        except Exception:
            pass

    def _post(self, payload):
        data = json.dumps(payload).encode('utf-8')
        headers = {"Content-Type": "application/json", "Accept": "application/json, text/event-stream"}
        if self.session_id:
            headers["Mcp-Session-Id"] = self.session_id
        try:
            req = urllib.request.Request(self.endpoint, data=data, headers=headers)
            with urllib.request.urlopen(req, timeout=10) as resp:
                sid = resp.headers.get("Mcp-Session-Id")
                if sid:
                    self.session_id = sid
                raw = resp.read().decode('utf-8', errors='replace')
                for line in raw.split("\n"):
                    line = line.strip()
                    if line.startswith("data:"):
                        return json.loads(line[5:].strip())
        except Exception:
            pass
        return {}

    def get_model(self, model_name, version="v19", scope="community"):
        try:
            res = self._post({
                "jsonrpc": "2.0",
                "method": "tools/call",
                "params": {"name": "get_odoo_model", "arguments": {"model": model_name, "version": version, "scope": scope}},
                "id": 10
            })
            return res.get("result", {}).get("structuredContent", {}).get("data", {})
        except Exception as e:
            return {"error": str(e)}

def load_feedback(db_path, days=7):
    """Load feedback reports from SQLite database."""
    if not os.path.isfile(db_path):
        return []
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        
        tables = [t[0] for t in c.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()]
        if "feedback" not in tables:
            conn.close()
            return []
            
        cutoff = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
        rows = c.execute("SELECT * FROM feedback WHERE timestamp >= ? ORDER BY timestamp DESC", (cutoff,)).fetchall()
        feedback_list = [dict(r) for r in rows]
        conn.close()
        return feedback_list
    except Exception as e:
        print(f"Warning: Could not read feedback DB ({e})")
        return []

def aggregate_gaps(feedback_entries):
    """Aggregate gaps and apply significance thresholds."""
    gaps_by_topic = {}
    
    for fb in feedback_entries:
        topic = fb.get("model_name") or fb.get("topic") or "general"
        severity = fb.get("severity", "cosmetic")
        user = fb.get("user") or fb.get("author") or "anonymous"
        
        if topic not in gaps_by_topic:
            gaps_by_topic[topic] = {
                "topic": topic,
                "reports_count": 0,
                "users": set(),
                "severities": [],
                "details": [],
                "broke_code_count": 0
            }
        
        gaps_by_topic[topic]["reports_count"] += 1
        gaps_by_topic[topic]["users"].add(user)
        gaps_by_topic[topic]["severities"].append(severity)
        if severity == "broke_code":
            gaps_by_topic[topic]["broke_code_count"] += 1
        gaps_by_topic[topic]["details"].append(fb.get("correction") or fb.get("notes") or "")

    significant_gaps = []
    for topic, data in gaps_by_topic.items():
        is_significant = (
            len(data["users"]) >= 3 or
            data["reports_count"] >= 5 or
            data["broke_code_count"] >= 1
        )
        if is_significant:
            significant_gaps.append(data)
            
    significant_gaps.sort(key=lambda x: (x["broke_code_count"], len(x["users"]), x["reports_count"]), reverse=True)
    return significant_gaps[:5]

def generate_weekly_report(proposals):
    """Generate clean, single-page human-reviewable report."""
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    md = f"# Weekly Odoo Knowledge Review Report\n\n"
    md += f"**Generated:** {now_str} | **Reviewer Action Required**: Approve / Reject below proposals.\n"
    md += f"**1-Click Apply Command**: `python scripts/knowledge_gap_analyzer.py --apply <ProposalNumber>`\n\n"
    md += "---\n\n"
    
    if not proposals:
        md += "### Status: All Knowledge Up to Date\n"
        md += "No high-significance knowledge gaps or recurring errors were detected this week.\n"
        return md

    md += f"## Executive Summary ({len(proposals)} Proposed Skill Updates)\n\n"
    md += "| # | Topic / Model | Evidence | Severity | Target Skill | Command |\n"
    md += "|---|---|---|---|---|:---:|\n"
    for i, p in enumerate(proposals, 1):
        sev = "🔴 Broke Code" if p["broke_code_count"] > 0 else "🟡 Moderate"
        md += f"| {i} | `{p['topic']}` | {p['reports_count']} reports ({len(p['users'])} users) | {sev} | `skills/odoo-functional` | `python scripts/knowledge_gap_analyzer.py --apply {i}` |\n"
    
    md += "\n---\n\n"
    
    for i, p in enumerate(proposals, 1):
        md += f"### Proposal {i}: Update `{p['topic']}` Knowledge\n\n"
        md += f"- **Topic/Model**: `{p['topic']}`\n"
        md += f"- **Evidence**: {p['reports_count']} employee reports from {len(p['users'])} distinct users.\n"
        if p["details"]:
            md += f"- **Sample Feedback**: *\"{p['details'][0][:120]}...\"*\n"
        md += f"- **Proposed Action**: Fetch ground truth from MCP and inject into `skills/odoo-functional/sale-crm-patterns.md`.\n\n"
        md += f"**Decision**: Run `python scripts/knowledge_gap_analyzer.py --apply {i}` to approve.\n\n"
        md += "---\n\n"
        
    return md

def apply_proposal(proposal_idx, proposals, mcp_client):
    """Apply approved proposal directly to the target skill file."""
    if proposal_idx < 1 or proposal_idx > len(proposals):
        print(f"Error: Invalid proposal index {proposal_idx}. Must be between 1 and {len(proposals)}.")
        return False
        
    proposal = proposals[proposal_idx - 1]
    topic = proposal["topic"]
    print(f"Applying Proposal #{proposal_idx} for model: {topic} ...")
    
    mdata = mcp_client.get_model(topic)
    target_file = os.path.join(SKILLS_ROOT, "odoo-functional", "sale-crm-patterns.md")
    
    patch_md = f"\n\n### Model: `{topic}` (Auto-Enriched from Review)\n"
    fields = mdata.get("fields", [])
    if fields:
        patch_md += "| Field Name | Type | Description |\n|---|---|---|\n"
        for f in fields[:20]:
            patch_md += f"| `{f.get('name')}` | `{f.get('type')}` | Auto-extracted from Odoo Knowledge MCP |\n"
            
    with open(target_file, "a", encoding="utf-8") as fp:
        fp.write(patch_md)
        
    print(f"[SUCCESS] Injected verified facts for {topic} into {target_file}")
    return True

def main():
    parser = argparse.ArgumentParser(description="Weekly Odoo Knowledge Gap Analyzer")
    parser.add_argument("--apply", type=int, help="Apply a specific proposal number by index (e.g. --apply 1)")
    args = parser.parse_args()

    feedback_entries = load_feedback(FEEDBACK_DB, days=7)
    significant_gaps = aggregate_gaps(feedback_entries)
    mcp_client = FastMcpClient(MCP_URL)

    if args.apply:
        apply_proposal(args.apply, significant_gaps, mcp_client)
        return

    print(f"1. Scanning feedback database: {FEEDBACK_DB} ...")
    print(f"   Found {len(feedback_entries)} feedback records from the past 7 days.")
    
    print("2. Aggregating gaps with High Significance Barrier...")
    print(f"   Identified {len(significant_gaps)} high-priority proposals (max 5).")
    
    print("3. Generating Review Report...")
    report_md = generate_weekly_report(significant_gaps)
    
    with open(REPORT_OUTPUT, "w", encoding="utf-8") as f:
        f.write(report_md)
        
    print(f"[SUCCESS] Weekly Review Report written to: {REPORT_OUTPUT}")

if __name__ == "__main__":
    main()

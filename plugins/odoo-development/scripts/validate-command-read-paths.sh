#!/usr/bin/env sh
set -eu

ROOT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
STATUS=0

resolve_ref() {
  ref_path=$1
  case "$ref_path" in
    odoo-development/*)
      ref_path=${ref_path#odoo-development/}
      ;;
  esac

  if printf '%s' "$ref_path" | grep -q '{version}'; then
    pattern=$(printf '%s' "$ref_path" | sed 's/{version}/*/g')
    set -- "$ROOT_DIR"/$pattern
    [ -e "$1" ]
    return
  fi

  [ -f "$ROOT_DIR/$ref_path" ]
}

for file in "$ROOT_DIR"/commands/*.md; do
  [ -f "$file" ] || continue
  tmp_refs=$(mktemp)
  sed -n 's/^Read:[[:space:]]*//p' "$file" > "$tmp_refs"

  if [ ! -s "$tmp_refs" ]; then
    rm -f "$tmp_refs"
    continue
  fi

  while IFS= read -r path; do
    path=$(printf '%s' "$path" | sed 's/[[:space:]]*$//')
    [ -n "$path" ] || continue
    if ! resolve_ref "$path"; then
      printf 'Missing referenced file in %s: %s\n' "$(basename "$file")" "$path"
      STATUS=1
    fi
  done < "$tmp_refs"
  rm -f "$tmp_refs"
done

if [ "$STATUS" -eq 0 ]; then
  echo "All Read: references in commands/*.md resolve correctly."
fi

exit "$STATUS"

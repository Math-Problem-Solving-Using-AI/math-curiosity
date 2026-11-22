#!/usr/bin/env bash
# Create a new problem repository next to this hub from template/.
# Usage: tools/new_problem.sh erdos-123    (OWNER defaults to the organization, override if needed)
set -euo pipefail
name="$1"
hub="$(cd "$(dirname "$0")/.." && pwd)"
dest="$hub/../$name"
owner="${OWNER:-Math-Problem-Solving-Using-AI}"
[ -e "$dest" ] && { echo "already exists: $dest"; exit 1; }
cp -r "$hub/template" "$dest"
cp "$hub/LICENSE" "$dest/LICENSE"
find "$dest" -type f \( -name '*.md' -o -name '*.txt' \) -print0 | xargs -0 sed -i \
  -e "s#{{NAME}}#$name#g" -e "s#{{HUB_URL}}#https://github.com/$owner/math-curiosity#g"
OWNER="$owner" "$hub/tools/sync_shared_docs.sh" "$dest"
git -C "$dest" init -q -b main
echo "created $dest. Next: fill README.md and steps/01, then commit."

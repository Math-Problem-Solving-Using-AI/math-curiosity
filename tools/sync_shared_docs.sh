#!/usr/bin/env bash
# Copy the canonical docs of this hub into docs/shared/ of each given problem repository.
# Usage: tools/sync_shared_docs.sh ../eq-unary-magma-laws ../eq-laws-without-small-models
set -euo pipefail
hub="$(cd "$(dirname "$0")/.." && pwd)"
owner="${OWNER:-Math-Problem-Solving-Using-AI}"
for dest in "$@"; do
  mkdir -p "$dest/docs/shared"
  for f in VERIFICATION_PROTOCOL LEAN_CAVEATS STEP_TEMPLATE LESSONS; do
    {
      printf '<!-- Canonical copy: https://github.com/%s/math-curiosity (docs/). Synced by tools/sync_shared_docs.sh.\n     Do not edit this copy, change the hub and sync. -->\n\n' "$owner"
      sed -e 's#docs/VERIFICATION_PROTOCOL.md#docs/shared/VERIFICATION_PROTOCOL.md#g' \
          -e 's#docs/LEAN_CAVEATS.md#docs/shared/LEAN_CAVEATS.md#g' \
          -e 's#docs/LESSONS.md#docs/shared/LESSONS.md#g' \
          -e 's#docs/STEP_TEMPLATE.md#docs/shared/STEP_TEMPLATE.md#g' \
          "$hub/docs/$f.md"
    } > "$dest/docs/shared/$f.md"
  done
  echo "synced $dest"
done

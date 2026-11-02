#!/bin/bash
# Set up a fresh machine for one es review shard (full/es/review/shards/shard-<k>.md). Usage:
#   HONEYEATER=/path/to/honeyeater-clone scripts/review-shard-setup.sh <k>
# Needs: a clone of honeyeater (any branch; pinned below), uv. Idempotent: rerun after any interruption.
# Leaves: $WORK/config.json (the review runner's config), the runtime, the lemma wheel, the uplift review scripts,
# the corpus sample for examples, and $WORK/routed.tsv (this shard's screening pool).
set -euo pipefail
K=$1
HE_COMMIT=c07c701585902f15fee2ef96a45893b1a5476940     # the counting runtime (shards are stamped with it)
WHEEL=honeyeater_lemma_es-1.5.0-py3-none-any.whl
WHEEL_SHA=89ddf9f6ebda6dc32a6ff156634030f228c855f00ecbc3d08b57935dba2a92e1
FQ=$(cd "$(dirname "$0")/.." && pwd)
WORK=${WORK:-$HOME/es-review-$K}
mkdir -p "$WORK/sample/work" "$WORK/sample/counts"

# 1. the pinned runtime
git -C "$HONEYEATER" fetch -q origin "$HE_COMMIT" || git -C "$HONEYEATER" fetch -q origin
[ -d "$WORK/he" ] || git -C "$HONEYEATER" worktree add --detach "$WORK/he" "$HE_COMMIT"
(cd "$WORK/he/backend" && uv sync -q)
PY=$WORK/he/backend/.venv/bin/python

# 2. the lemma release, from this repository's setup branch, checked against its sha256
if [ ! -f "$WORK/$WHEEL" ]; then
  git -C "$FQ" fetch -q origin es-shards-setup
  git -C "$FQ" show "origin/es-shards-setup:wheels/$WHEEL" > "$WORK/$WHEEL"
fi
echo "$WHEEL_SHA  $WORK/$WHEEL" | sha256sum -c -
[ -d "$WORK/site/honeyeater_lemma_es" ] || uv pip install -q --python "$PY" --target "$WORK/site" --no-deps "$WORK/$WHEEL"

# 3. the review runner (uplift f8c8a67) and the fixed example extractor (forms with >= 10 % of the lemma's count)
git -C "$FQ" fetch -q origin uplift
[ -d "$WORK/up" ] || git -C "$FQ" worktree add --detach "$WORK/up" f8c8a67
cp "$FQ/review/scripts/examples10.py" "$WORK/up/scripts/review/examples10.py"

# 4. config: prompts from uplift's scripts/review/prompts/es; window 40k; the corpus sample spec is fixed
cat > "$WORK/config.json" <<JSON
{"lang": "es", "language_name": "Spanish", "work": "$WORK", "counts": "$WORK/none",
 "honeyeater": "$WORK/he", "lemma_dir": "$WORK/site/honeyeater_lemma_es", "wheel": "$WORK/$WHEEL",
 "window": 41500, "sample": {"paracrawl-en-es": {"urls": [0], "max_chars": 300000000}},
 "rules": "prompts/es/rules-flagged.md", "rules_unflagged": "prompts/es/rules-unflagged.md",
 "screener": "prompts/es/screener.md", "reviewer_model": "sonnet", "adjudicator_model": "opus", "parallel": 6}
JSON
cp "$FQ/full/es/review/shards/shard-$K/routed.tsv" "$WORK/routed.tsv"

# 5. the corpus sample (ParaCrawl r9 en-es, first 300M kept characters, plus Tatoeba whole: deterministic;
#    the hygiene and shard code of the count). About 10 minutes; nothing from it is committed.
export PYTHONPATH=.:$FQ:$WORK/site:$WORK/up/scripts/review
cd "$WORK/he/backend"
ls "$WORK/sample/work/"*.done.json >/dev/null 2>&1 && [ "$(ls "$WORK/sample/work/"*.done.json | wc -l)" -ge 2 ] || \
  "$PY" "$WORK/up/scripts/review/sample.py" "$WORK/config.json"
echo "ready: WORK=$WORK PY=$PY (PYTHONPATH=$PYTHONPATH; run the scripts from $WORK/he/backend)"

#!/bin/bash
# Count one part of a distributed frequer run on a fresh machine and ship its shard counts home.
# README §Distributed counting. Usage:
#   HONEYEATER=/path/to/honeyeater-clone scripts/remote-part.sh <lang> <i/N> <workers>
# Needs: a clone of honeyeater (any branch; it is pinned below), uv, git push access to this repository.
set -euo pipefail
LANG_CODE=$1; PART=$2; WORKERS=${3:-4}
HE_COMMIT=c07c701585902f15fee2ef96a45893b1a5476940          # the counting runtime; shards are stamped with it
WHEEL=honeyeater_lemma_ja-1.5.0-py3-none-any.whl
WHEEL_SHA=742044e86967a1cec324c9773881c4a5684166de9f7ebae880472e542fa46ac1
FQ=$(cd "$(dirname "$0")/.." && pwd)
WORK=${WORK:-$HOME/frequer-part}
mkdir -p "$WORK"

# 1. the pinned runtime: a detached, clean worktree at HE_COMMIT, with the Japanese dictionary group
git -C "$HONEYEATER" fetch -q origin "$HE_COMMIT" || git -C "$HONEYEATER" fetch -q origin
[ -d "$WORK/he" ] || git -C "$HONEYEATER" worktree add --detach "$WORK/he" "$HE_COMMIT"
(cd "$WORK/he/backend" && uv sync -q --group nlp-models)
PY=$WORK/he/backend/.venv/bin/python

# 2. the lemma release (not in R2): from this repository's setup branch, checked against its sha256
if [ ! -f "$WORK/$WHEEL" ]; then
  git -C "$FQ" fetch -q origin "${LANG_CODE}-shards-setup"
  git -C "$FQ" show "origin/${LANG_CODE}-shards-setup:wheels/$WHEEL" > "$WORK/$WHEEL"
fi
echo "$WHEEL_SHA  $WORK/$WHEEL" | sha256sum -c -
[ -d "$WORK/site/honeyeater_lemma_$LANG_CODE" ] || uv pip install -q --python "$PY" --target "$WORK/site" --no-deps "$WORK/$WHEEL"
[ -d "$WORK/deps/zstandard" ] || uv pip install -q --python "$PY" --target "$WORK/deps" zstandard

# 3. count this part (resumable: rerun this script after any interruption), then ship until done or told to stop
export PYTHONPATH=.:$FQ:$WORK/site FREQUER_DEPS=$WORK/deps OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
cd "$WORK/he/backend"
setsid "$PY" -m frequer count "$LANG_CODE" --data-dir "$WORK/data" --workers "$WORKERS" --part "$PART" --no-cooc \
  --lemma-dir "$WORK/site/honeyeater_lemma_$LANG_CODE" --wheel "$WORK/$WHEEL" >> "$WORK/count.log" 2>> "$WORK/count.err" &
COUNT_PID=$!
echo "count pid $COUNT_PID; log $WORK/count.log"
"$PY" -m frequer ship "$LANG_CODE" --data-dir "$WORK/data" --repo "$WORK/shiprepo" --part "$PART" --count-pid "$COUNT_PID"

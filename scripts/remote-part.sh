#!/bin/bash
# Count one part of a distributed frequer run on a fresh machine and ship its shard counts home.
# README §Distributed counting. Usage:
#   HONEYEATER=/path/to/honeyeater-clone scripts/remote-part.sh <lang> <i/N> <workers>
# Needs: a clone of honeyeater (any branch; it is pinned below), uv, git push access to this repository.
set -euo pipefail
LANG_CODE=$1; PART=$2; WORKERS=${3:-4}
HE_COMMIT=c07c701585902f15fee2ef96a45893b1a5476940          # the counting runtime; shards are stamped with it
case "$LANG_CODE" in   # the lemma release each language counts with (its wheel is on <lang>-shards-setup)
  ja) WHEEL=honeyeater_lemma_ja-1.5.0-py3-none-any.whl
      WHEEL_SHA=742044e86967a1cec324c9773881c4a5684166de9f7ebae880472e542fa46ac1
      SYNC_GROUP=(--group nlp-models) ;;   # the Japanese dictionary
  es) WHEEL=honeyeater_lemma_es-1.5.0-py3-none-any.whl
      WHEEL_SHA=89ddf9f6ebda6dc32a6ff156634030f228c855f00ecbc3d08b57935dba2a92e1
      SYNC_GROUP=() ;;
  zh) WHEEL=honeyeater_lemma_zh-1.6.4-py3-none-any.whl
      WHEEL_SHA=27abd5c0320580550aad309c25eab062f1f53dd15f6132650a454b7858d75f91
      HE_COMMIT=8bc18170ed9879c892d86445e8f11de9522975af   # Honeyeater main pinning zh 1.6.4 (jieba-zh + segmenter)
      SYNC_GROUP=() ;;
  de) WHEEL=honeyeater_lemma_de-1.5.1-py3-none-any.whl
      WHEEL_SHA=f14d4d64be671ac155c5dc6f9c67d98e851ee9e507e27c2705ad0338c27f7822
      SYNC_GROUP=() ;;
  *)  echo "no wheel recorded for $LANG_CODE" >&2; exit 1 ;;
esac
SPACY_DE=de_core_news_sm-3.8.0-py3-none-any.whl   # the German backend's model (senter); a GitHub-release wheel
SPACY_DE_SHA=fec69fec52b1780f2d269d5af7582a5e28028738bd3190532459aeb473bfa3e7
FQ=$(cd "$(dirname "$0")/.." && pwd)
WORK=${WORK:-$HOME/frequer-part}
mkdir -p "$WORK"

# 1. the pinned runtime: a detached, clean worktree at HE_COMMIT (with the Japanese dictionary group)
git -C "$HONEYEATER" fetch -q origin "$HE_COMMIT" || git -C "$HONEYEATER" fetch -q origin
[ -d "$WORK/he" ] || git -C "$HONEYEATER" worktree add --detach "$WORK/he" "$HE_COMMIT"
(cd "$WORK/he/backend" && uv sync -q "${SYNC_GROUP[@]}")
PY=$WORK/he/backend/.venv/bin/python

# 2. the lemma release (not in R2): from this repository's setup branch, checked against its sha256
if [ ! -f "$WORK/$WHEEL" ]; then
  git -C "$FQ" fetch -q origin "${LANG_CODE}-shards-setup"
  git -C "$FQ" show "origin/${LANG_CODE}-shards-setup:wheels/$WHEEL" > "$WORK/$WHEEL"
fi
echo "$WHEEL_SHA  $WORK/$WHEEL" | sha256sum -c -
[ -d "$WORK/site/honeyeater_lemma_$LANG_CODE" ] || uv pip install -q --python "$PY" --target "$WORK/site" --no-deps "$WORK/$WHEEL"
if [ "$LANG_CODE" = de ] && ! "$PY" -c "import de_core_news_sm" 2>/dev/null; then
  # from the setup branch (sandbox proxies may block GitHub release downloads), checked against its sha256
  git -C "$FQ" fetch -q origin de-shards-setup
  git -C "$FQ" show "origin/de-shards-setup:wheels/$SPACY_DE" > "$WORK/$SPACY_DE"
  echo "$SPACY_DE_SHA  $WORK/$SPACY_DE" | sha256sum -c -
  uv pip install -q --python "$PY" "$WORK/$SPACY_DE"
fi
# shards the coordinator counted before the run was distributed (deterministic names): cut past, never counted
SKIP=()
if git -C "$FQ" show "origin/${LANG_CODE}-shards-setup:skip/$LANG_CODE.txt" > "$WORK/skip.txt" 2>/dev/null; then
  SKIP=(--skip-file "$WORK/skip.txt")
fi
[ -d "$WORK/deps/zstandard" ] || uv pip install -q --python "$PY" --target "$WORK/deps" zstandard

# 3. count this part (resumable: rerun this script after any interruption), then ship until done or told to stop
export PYTHONPATH=.:$FQ:$WORK/site FREQUER_DEPS=$WORK/deps OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
cd "$WORK/he/backend"
setsid "$PY" -m frequer count "$LANG_CODE" --data-dir "$WORK/data" --workers "$WORKERS" --part "$PART" --no-cooc "${SKIP[@]}" \
  --lemma-dir "$WORK/site/honeyeater_lemma_$LANG_CODE" --wheel "$WORK/$WHEEL" >> "$WORK/count.log" 2>> "$WORK/count.err" &
COUNT_PID=$!
echo "count pid $COUNT_PID; log $WORK/count.log"
"$PY" -m frequer ship "$LANG_CODE" --data-dir "$WORK/data" --repo "$WORK/shiprepo" --part "$PART" --count-pid "$COUNT_PID"

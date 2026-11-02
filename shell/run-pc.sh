#!/bin/bash
source /home/user/env.sh
while pgrep -f "sources tatoeba-spa" >/dev/null; do sleep 15; done
exec $PY -m frequer count es --data-dir /home/user/data --workers 3 --sources paracrawl-en-es --checkpoints --out-dir /home/user/out/es $LEMMA

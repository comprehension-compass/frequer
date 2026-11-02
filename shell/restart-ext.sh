#!/bin/bash
# Restart the extended count (part 0/5), its coordinator and the convergence pusher after a worker restart.
cd /home/user/he-c07c701/backend
export PYTHONPATH=.:/home/user/fq-ext:/home/user/wheel-site
L="--lemma-dir /home/user/wheel-site/honeyeater_lemma_es --wheel /home/user/wheels/honeyeater_lemma_es-1.5.0-py3-none-any.whl"
setsid nohup .venv/bin/python -m frequer count es --data-dir /home/user/data --workers 2 --part 0/5 $L >> /home/user/out/count-p0.log 2>> /home/user/out/count-p0.err < /dev/null &
sleep 5
P=$(pgrep -f "^.venv/bin/python -m frequer count es" | head -1)
echo "count pid $P"
setsid nohup .venv/bin/python -m frequer coordinate es --data-dir /home/user/data --repo /home/user/coord-repo --parts 5 --out-dir /home/user/out/es-ext --local-pid $P $L >> /home/user/out/coordinate.log 2>&1 < /dev/null &
setsid nohup /home/user/pushconv-ext.sh > /home/user/out/pushconv-ext.log 2>&1 < /dev/null &
sleep 3
ps -eo pid,args | grep -E "frequer (count|coordinate)|pushconv" | grep -v grep | cut -c1-120

#!/bin/bash
# One cascade round up to the gate: screen the keeps new to the window, examples, reviewers (flagged + unflagged).
# Usage: cascade.sh <n>   (expects /home/user/zhrev/routed.tsv current; seen-lists in /home/user/zhrev/seen.txt)
set -euo pipefail
N=$1; Z=/home/user/zhrev; R=/home/user/frequer/scripts/review
export PYTHONPATH=.:/home/user/frequer:/home/user/site:$R FREQUER_DEPS=/home/user/fdeps OMP_NUM_THREADS=1
cd /home/user/he-8bc1817/backend
python3 - "$N" <<'PY'
import sys,json,os
n=sys.argv[1]; Z='/home/user/zhrev'
seen=set(open(f'{Z}/seen.txt').read().split())
rows=[l for l in open(f'{Z}/routed.tsv')]
new=[l for l in rows[1:] if int(l.split('\t')[7])<=40500 and l.split('\t')[2]=='keep' and l.split('\t')[1] not in seen]
d=f'{Z}/s{n}'; os.makedirs(d,exist_ok=True)
with open(f'{d}/routed.tsv','w') as f:
    f.write(rows[0])
    for i,l in enumerate(new,1):
        p=l.rstrip('\n').split('\t'); p[7]=str(i); f.write('\t'.join(p)+'\n')
c=json.load(open(f'{Z}/config.json')); c['work']=d; json.dump(c,open(f'{d}/config.json','w'),ensure_ascii=False)
open(f'{Z}/seen.txt','a').write(''.join(l.split('\t')[1]+'\n' for l in new))
print('new keeps',len(new))
PY
(cd $R && python3 screen.py $Z/s$N/config.json screen$N > $Z/s$N/screen.log 2>&1) &
.venv/bin/python $R/examples.py $Z/config.json $Z/r$N.tsv --actions pending 2>&1 | grep -v '"event"' | tail -1
wait
grep -E '"(screened|candidates)"' $Z/s$N/screen.log
if [ -s $Z/s$N/screen$N/candidates.txt ]; then
  .venv/bin/python $R/examples.py $Z/config.json $Z/s$N.tsv --only-file $Z/s$N/screen$N/candidates.txt --notes $Z/s$N/screen$N/candidates.tsv 2>&1 | grep -v '"event"' | tail -1
fi
cd $R
python3 review.py $Z/config.json $Z/r$N.tsv round$N --decisions keep,drop,merge 2>&1 | grep -E '"(lemmas|agreed|to_adjudicator)"' &
[ -s $Z/s$N.tsv ] && python3 review.py $Z/config.json $Z/s$N.tsv screen$N --rules prompts/zh/rules-unflagged.md --decisions keep,drop,merge 2>&1 | grep -E '"(lemmas|agreed|to_adjudicator)"' &
wait

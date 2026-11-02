#!/bin/bash
# Push out/es-ext/convergence.{md,json} to full-es (as full/es/convergence-ext.*) whenever they change.
cd /home/user/push-repo
while true; do
  if [ -f /home/user/out/es-ext/convergence.md ] && ! cmp -s /home/user/out/es-ext/convergence.md full/es/convergence-ext.md; then
    cp /home/user/out/es-ext/convergence.md full/es/convergence-ext.md
    cp /home/user/out/es-ext/convergence.json full/es/convergence-ext.json
    rows=$(grep -c '^| [0-9]' full/es/convergence-ext.md)
    git add full/es/convergence-ext.md full/es/convergence-ext.json
    git commit -q -m "es extension convergence (filtered list): $rows checkpoints" -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01LCaNDxgx4QeyJKvxvbEYHU"
    for d in 2 4 8 16; do git pull -q --rebase origin full-es && git push -q origin full-es && break; sleep $d; done
  fi
  sleep 120
done

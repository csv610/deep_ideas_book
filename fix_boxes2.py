#!/usr/bin/env python3
import os, re, glob

chapters_dir = "chapters"
macros = [
    'historicalbox', 'highlightbox', 'roadblockbox', 'connectionbox',
    'mentalLeap', 'question', 'roadblock', 'connection', 'historicalnoteMacro',
]

for fp in sorted(glob.glob(os.path.join(chapters_dir, '*.tex'))):
    with open(fp) as f:
        c = f.read()
    o = c
    # 1. collapse doubled backslashes on our macros: \\macro -> \macro
    for m in macros:
        c = c.replace('\\\\' + m, '\\' + m)
    # 2. remove a stray '}' sitting alone on its own line (leftover from old arg syntax)
    c = re.sub(r'^\s*\}\s*$', '', c, flags=re.MULTILINE)
    if c != o:
        with open(fp, 'w') as f:
            f.write(c)
        print('Fixed:', os.path.basename(fp))
    else:
        print('OK:   ', os.path.basename(fp))
print('Done.')

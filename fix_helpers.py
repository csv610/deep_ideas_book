#!/usr/bin/env python3
import os, re, glob

chapters_dir = "chapters"
# helper macros still used in command form: \macro{body}
helpers = ['question', 'roadblock', 'historicalnoteMacro', 'connection', 'mentalLeap']

for fp in sorted(glob.glob(os.path.join(chapters_dir, '*.tex'))):
    if os.path.basename(fp) == 'chapter_template.tex':
        continue
    with open(fp) as f:
        c = f.read()
    o = c
    for m in helpers:
        # \macro[opt]{body}  -> environment (opt rarely used by these)
        c = re.sub(
            r'\\' + m + r'\[([^\]]*)\]\{([^{}]*)\}',
            lambda mm: r'\begin{' + m + r'}[' + mm.group(1) + r']' + mm.group(2).strip() + r'\end{' + m + r'}',
            c)
        # \macro{body}  -> \begin{macro} body \end{macro}   (body has no nested braces)
        c = re.sub(
            r'\\' + m + r'\{([^{}]*)\}',
            lambda mm: r'\begin{' + m + r'}' + mm.group(1).strip() + r'\end{' + m + r'}',
            c)
    if c != o:
        with open(fp, 'w') as f:
            f.write(c)
        print('Converted:', os.path.basename(fp))
    else:
        print('OK:       ', os.path.basename(fp))
print('Done.')

#!/usr/bin/env python3
import os, re, glob

chapters_dir = "chapters"
# macros that appear as \macro[opt]{body} or \macro{body}
box_macros = ['historicalbox', 'highlightbox', 'roadblockbox', 'connectionbox', 'mentalLeap']

for fp in sorted(glob.glob(os.path.join(chapters_dir, '*.tex'))):
    if os.path.basename(fp) == 'chapter_template.tex':
        continue
    with open(fp) as f:
        c = f.read()
    o = c
    for m in box_macros:
        # \macro[title]{body}  -> \begin{macro}[title] body \end{macro}
        c = re.sub(
            r'\\' + m + r'\[([^\]]*)\]\{(.*?)\}',
            lambda mm: r'\begin{' + m + r'}[' + mm.group(1) + r']' + mm.group(2).strip() + r'\end{' + m + r'}',
            c, flags=re.DOTALL)
        # \macro{body}  -> \begin{macro} body \end{macro}
        c = re.sub(
            r'\\' + m + r'\{(.*?)\}',
            lambda mm: r'\begin{' + m + r'}' + mm.group(1).strip() + r'\end{' + m + r'}',
            c, flags=re.DOTALL)
    if c != o:
        with open(fp, 'w') as f:
            f.write(c)
        print('Converted:', os.path.basename(fp))
    else:
        print('OK:       ', os.path.basename(fp))
print('Done.')

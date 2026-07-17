#!/usr/bin/env python3
import re, os

chapters_dir = "chapters"
box_types = ['historicalbox','highlightbox','roadblockbox','connectionbox']

for fn in sorted(os.listdir(chapters_dir)):
    if not fn.endswith('.tex') or fn == 'chapter_template.tex':
        continue
    fp = os.path.join(chapters_dir, fn)
    with open(fp) as f:
        c = f.read()
    o = c

    # Remove stray } lines
    c = re.sub(r'^[ \t]*\}[ \t]*$', '', c, flags=re.MULTILINE)

    # Convert environment syntax to command syntax
    for box in box_types:
        endtag = r'\end{' + box + '}'
        begintag = r'\begin{' + box + '}'

        # With title: \begin{box}[title] content \end{box}
        c = re.sub(
            r'\\begin\{' + box + r'\}\[([^\]]*)\](.*?)\\end\{' + box + r'\}',
            lambda m: r'\\' + box + r'[' + m.group(1) + r']{' + m.group(2).strip() + r'}',
            c, flags=re.DOTALL
        )
        # Without title: \begin{box} content \end{box}
        c = re.sub(
            r'\\begin\{' + box + r'\}(.*?)\\end\{' + box + r'\}',
            lambda m: r'\\' + box + r'{' + m.group(1).strip() + r'}',
            c, flags=re.DOTALL
        )

    if c != o:
        with open(fp, 'w') as f:
            f.write(c)
        print(f'Fixed: {fn}')
    else:
        print(f'OK:   {fn}')

print('\nDone!')
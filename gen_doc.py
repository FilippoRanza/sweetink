#! /usr/bin/python

"""
Generate a Markdown file including a latex file.
Used to generate markdown for github pages, containing
code from some tex file
"""

from os.path import join

def make_md(title, tex_file):
    out = f'# Template Frontespizio Tesi {title}\n\n'
    out += '```latex\n'
    with open(tex_file) as f:
        out += f.read()

    out += '\n```'
    return out

def process_file(title, name):
    out = make_md(title, name)
    s = name.index('_') + 1
    e = name.index('.')
    out_name = join('docs', name[s:e] + '.md')
    with open(out_name, 'w') as f:
        print(out, file=f) 


def main():
    process_file('Magistrale', 'frontespizio_magistrale.tex')
    process_file('Triennale', 'frontespizio_triennale.tex')


if __name__ == "__main__":
    main()


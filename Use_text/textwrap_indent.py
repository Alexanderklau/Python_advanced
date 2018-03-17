#coding: utf-8
__author__ = "Yemilice_lau"


import textwrap
from textwrap_example import sample_text


dedented_text = textwrap.dedent(sample_text)
wrapped = textwrap.fill(dedented_text, width=60)
wrapped += '\nSecond paragraph after a blank line.'
final = textwrap.indent(wrapped, '> ')

print('Quoted block:\n')
print(final)
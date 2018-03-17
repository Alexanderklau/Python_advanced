#coding: utf-8
__author__ = "Yemilice_lau"


import textwrap
from textwrap_example import sample_text

dedented_text = textwrap.dedent(sample_text)
print('Dedented:')
print(dedented_text)
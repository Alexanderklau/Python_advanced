# coding: utf-8
__author__ = 'lau.wenbo'

"""
search() 就是个查找的玩意儿，找到返回一个match，找不到返回一个None, 查找很有用
"""

import re

patten = 'this'
text = 'Does this text match the patten?'

match = re.search(patten, text)

print('{this} and {test}'.format(this=1,test=2))
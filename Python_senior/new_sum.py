# coding: utf-8
__author__ = 'lau.wenbo'


def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head


items = [1, 2, 3]
print(sum(items))

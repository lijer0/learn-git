#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def hanno(n, a='A', b='B', c='C'):
    if n == 1:
        print('move', a, '-->', c)
    else:
        hanno(n-1, a, c, b)
        hanno(1, a, b, c)
        hanno(n-1, b, a, c)
hanno(int(input('汉诺塔：请输入第一柱盘子数')))

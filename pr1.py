#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-26 10:05:48
# @Author  : Garvit Kansal (helewrer3@gmail.com)
# @Link    : NULL
# @Version : 1.0.0

import sys
def calc(n):
    ans = 0
    for i in range(n):
        if i%3 == 0:
            ans = ans + i
        elif i%5 == 0:
            ans = ans + i
    print(ans)

if __name__ == '__main__':
    #Accept user input and call calc()
    x = int(input(""))
    calc(x)
    sys.exit(0)

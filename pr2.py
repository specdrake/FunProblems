#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-26 10:30:23
# @Author  : Garvit Kansal (helewrer3@gmail.com)
# @Link    : NULL
# @Version : 1.0.0

import sys
def calc(n):
    a = 0
    b = 1
    if n < 0: 
        print("Incorrect input") 
    elif n == 0: 
        print(a)
    else: 
        for i in range(2,n): 
            c = a + b 
            a = b 
            b = c 
            if b%2 == 0:
                print(b)
 

if __name__ == '__main__':
    #Accept user input and call calc()
    x = input("")
    calc(x)
    sys.exit(0)
#!/usr/bin/env python
import sys

'''
def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

print fib(100)
'''

def fib():
    a, b = 0, 1
    while 1:
        yield a
        a, b = b, a + b

a = fib()
i = 0
while 1:
    temp = a.next()
    if len(str(temp)) == 1000:
        print i
        sys.exit()
    i += 1

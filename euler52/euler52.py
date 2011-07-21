#!/usr/bin/env python
import sys

def same(i, j):
    i = list(str(i))
    j = list(str(j))

    if len(i) != len(j): return False

    while len(i) > 0:
        try:
            j.remove(i.pop())
        except ValueError:
            return False
    
    return True

def test(i):
    return same(i, i*2) and same(i, i*3) and same(i, i*4) and same(i, i*5) and same(i, i*6)

min = 0
i = 1
while i < 1000000:
    if test(i): 
        print i
        sys.exit()
    i += 1
        

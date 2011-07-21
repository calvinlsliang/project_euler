#!/usr/bin/env python
import Calvin

def check(n):
    b = n
    i = 0
    while len(b) > 0:
        if not Calvin.prime(int(b)): return False
        if len(b) == 1: return Calvin.prime(int(b))
        else: b = str(int(b[1:]))

    c = n
    i = 0
    while len(c) > 0:
        if not Calvin.prime(int(c)): return False
        if len(c) == 1: return Calvin.prime(int(c))
        c = str(int(c[:len(c)-1]))
    return True


s = []
f = open('prime')
a = f.readline().split()
a = a[4:]
for i in a:
    if check(i): s.append(i)

sum = 0
for i in s
    sum += int(i)

print sum

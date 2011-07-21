#!/usr/bin/env python
import time

def pythag(a, b, c):
    return c*c == a*a + b*b and a + b > c

start = time.time()
'''
s = []
p = 1001
max, maxp = 0, []
peri = 1
while peri < p:
    a = 1
    while a < peri/3:
        b = a
        while b <= (peri - a)/2 :
            c = peri - a - b
            if pythag(a, b, c):
                s.append((a, b, c))
            b += 1
        a += 1
    if len(s) > max: max, maxp = len(s), s
    s = []
    peri += 1
'''
p = 1000
max = 0
peri = 1
periMax = 0
count = 0
while peri <= p:
    a = 1
    while a < peri/3:
        b = a
        while b <= (peri - a)/2 :
            c = peri - a - b
            if pythag(a, b, c):
                count += 1
            b += 1
        a += 1
    if count > max: max, periMax = count, peri
    peri += 1
    count = 0


print max, periMax
print time.time() - start
# don't know how to remove duplicate sets / too lazy to

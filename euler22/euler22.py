#!/usr/bin/env python
import re

def value(k):
    return ord(k) - ord('A') + 1

def name(s):
    sum = 0
    for i in range(len(s)):
        sum += value(s[i])
    return sum

f = open('names', 'r')

s = f.readline()
p = re.compile(r'","')
s = p.sub(' ', s)

a = s.split(' ')
a[0] = a[0][1:]
a[5162] = a[5162][:len(a[5162])-1]

a.sort()

sum = 0
for i, k in enumerate(a):
    print i, k
    sum += (i+1) * name(k)




print sum

f.close()

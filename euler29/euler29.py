#!/usr/bin/env python
s = []
for a in range(2, 101):
    for b in range(2, 101):
        s.append(a ** b)

s = list(set(s))
s.sort()
print len(s)

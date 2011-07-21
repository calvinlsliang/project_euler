#!/usr/bin/env python

def all_zero(l):
    i = 0
    while i < len(l):
        if l[i] != 0: return False
        i += 1
    return True

def pandigital(a, b, c):
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while a > 0:
        k = a % 10
        if k == 0: return False
        else: l[k - 1] -= k
        a /= 10
    while b > 0:
        k = b % 10
        if k == 0: return False
        else: l[k - 1] -= k
        b /= 10
    while c > 0:
        k = c % 10
        if k == 0: return False
        else: l[k - 1] -= k
        c /= 10
    if all_zero(l): return True
    else: return False

a = 10
b = 100
s = []
while a < 100 and a*b < 98765:
    b = 100
    while b < 1000 and a*b < 98765:
        if pandigital(a, b, a*b): s.append(a*b)
        b += 1
    a += 1

print s
print sum(s)

# print unique products only, not multiples

#!/usr/bin/env python

def month(n, ye):
    if n == 2:
        if ye % 4 == 0:
            if ye % 400 == 0: print ye; return 29
            else: return 28
        else: return 28
    elif n == 4 or n == 6 or n == 9 or n == 11: return 30
    else: return 31

sum = -1 #blah
day = 1
for ye in range(1901, 2001):
    for mo in range(1, 13):
        day += month(mo, ye)
        day = day % 7
        if day == 6: sum += 1

print sum, day

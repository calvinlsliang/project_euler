#!/usr/bin/env python
import Calvin

def check(n):
    t = n
    sum = 0
    while n != 0:
        f = Calvin.factorial(n % 10)
        sum += f
        n /= 10
    return t == sum


sum = 0
i = 3
while i < 100000:
    if check(i): sum += i
    i += 1

print sum

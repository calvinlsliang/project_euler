#!/usr/bin/env python

def check(n):
    orig = n
    sum = 0
    t = 0
    while n != 0:
        t = n % 10

        n /= 10
        sum += t ** 5
    return sum == orig

#print check(8207)

sum = 0
n = 2
while n < 10000000:
    if check(n):
        sum += n
    n += 1

print sum

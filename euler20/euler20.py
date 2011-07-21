#!/usr/bin/env python

def fact(n):
    if n == 0 or n == 1: return n
    else: return n * fact(n-1)

num = fact(100)
sum = 0
while num > 0:
    sum += num % 10
    num /= 10

print sum

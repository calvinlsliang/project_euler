#!/usr/bin/env python

sum, i = 0, 1
while i < 1001:
    sum += i**i
    i += 1

print sum % 10000000000

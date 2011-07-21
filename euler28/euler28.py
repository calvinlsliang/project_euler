#!/usr/bin/env python

spiral = 1001 # total number of rows
h = 0 # rows by 2
i = 3
sum = 0
m = 2 # multiplier
while h < (spiral - 1) / 2:
    
    t = (i + i + m * 3) * 2
    sum += t
    i += m * 3
    h += 1
    m += 2
    i += m


sum += 1
print sum

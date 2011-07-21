#!/usr/bin/env python
import Calvin
import math
'''
def rotate(arr):
    arr = str(arr)
    i = 0
    s = len(arr)
    a = []
    a.append(arr)
    while i < s-1:
        arr = arr[s-1] + arr[:s-1]
        a.append(arr)
        i += 1
    return a
'''

def contains_even(num):
    s = num
    while s != 0:
        if s%10 == 0 or s%10==2 or s%10==4 or s%10==6 or s%10==8: return True
        s /= 10
    return False

def rotate(arr):
    arr = str(arr)
    i = 0
    s = len(arr)
    if not check(int(arr)): return False
    while i < s-1:
        arr = arr[s-1] + arr[:s-1]
        if not check(int(arr)): return False
        i += 1
    return True

def check(n):
    for i in range(2, int(math.sqrt(n))+1):  
        if n % i == 0:       
            return False
    return True

count = 0

i = 1
while i < 1000000:
    if not contains_even(i):
        if rotate(i): 
            print i
            count += 1
    i += 1
print count



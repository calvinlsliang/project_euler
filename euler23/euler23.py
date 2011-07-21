#!/usr/bin/env python
import math

def abundant(n):
    c = 1
    i = 2
    j = math.sqrt(n)
    while (i <= int(j)):
        if i == j: c += i
        elif n % i == 0:
            c += i
            c += n / i
        i += 1
    return c > n

def abundant_list(n):
    f = [x for x in range(2, n + 1) if abundant(x)]
    return f

def binary_search(f, v):
    low = f[0]
    high = f[len(f) - 1]
    if low == high: return low
    while (low < high):
        mid = low + ((high - low) / 2)
        if (f[mid] < v): low = mid + 1
        else: high = mid
    if ((low <= f[len(f) - 1]) and f[low] == v): return low
    else: return -1

def search(f, v):
    i = 0
    while i < len(f):
        if f[i] == v: return v
        i += 1
    return -1
    
def sum(f, n):
    i = 1
    k = 0
    s = 0
    while i < n + 1:
        while f[k] < i / 2:
            if f[k] + search(f, n - f[k]) == i:
                break
            k += 1
            if k == n / 2: s += i
        i += 1
        k = 0
    return s
                
            
    

f = abundant_list(28123)
print sum(f, 28123)

    

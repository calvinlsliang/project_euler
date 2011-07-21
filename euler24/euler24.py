#!/usr/bin/env python
import array
import copy

def fact(n):
    if n == 1 or n == 0: return n
    else: return n * fact(n-1)

def permutation(index, s):
    arr = copy.copy(s)
    n = len(arr)
    f = fact(n - 1)

    i = 0
    while i < n-1:
        tempi = (index / f) % (n - i)
        temps = arr[i + tempi]

        j = i + tempi
        while j > i:
            arr[j] = arr[j-1]
            j -= 1

        arr[i] = temps
        f /= (n - i - 1)
        i += 1

    return arr

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print permutation(999999, a)

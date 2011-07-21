#!/usr/bin/env python
import re
import time

def triangle(n):
    s = []
    i = 1
    while i < n:
        t = (i * (i + 1)) / 2
        s.append(t)
        i += 1
    return s

def value(n):
    l = list(n)
    sum = 0
    for i in l:
        sum += ord(i) - ord('A') + 1
    return sum

def located(arr, n): # word value n located in triangle array arr
    for i in arr:
        if n == i: return True
    return False
    
start = time.time()

t = triangle(30)
count = 0

f = open('words.txt', 'r')

s = f.readline()
p = re.compile(r'","')
s = p.sub(' ', s)
a = s.split(' ')

a[0] = a[0][1:]
a[1785] = a[1785][:len(a[1785])-1]

for i in a:
    if located(t, value(i)): count += 1

print count

'''
for word in file('words.txt'):
    for c in word.rstrip():
        print c
'''

print str(time.time() - start)

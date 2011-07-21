#!/usr/bin/env python

s = ''
i = 1
while len(s) < 1000005:
    s += str(i)
    i += 1

print int(s[0]) * int(s[9]) * int(s[99]) * int(s[999]) * int(s[9999]) * int(s[99999]) * int(s[999999])

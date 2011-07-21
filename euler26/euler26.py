#!/usr/bin/env python
import decimal

def cycle(n):
    num = decimal.Decimal(1)/decimal.Decimal(n)
    print num
    if len(str(num)) < 500: return 0
    return 5

decimal.getcontext().prec=500
print cycle(8)

http://en.wikipedia.org/wiki/Recurring_decimal

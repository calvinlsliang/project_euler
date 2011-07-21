#!/usr/bin/env python

def dec2bin(dec):
    bin = ''
    while dec != 0:
        if dec % 2 == 0: bin = '0' + bin
        else: bin = '1' + bin
        dec /= 2

    return bin

def bin2dec(bin):
    dec = 0
    p = 0
    bin = int(bin)
    while bin != 0:
        if bin % 10 == 1: dec += 2 ** p
        bin /= 10
        p += 1
    return dec

def dec_palin(n): # decimal input
    return algo(str(n))

def bin_palin(n): # decimal input
    bin = dec2bin(n)
    return algo(bin)

def algo(bin): # decimal input
    bin = list(bin)
    t = bin[:len(bin)/2]
    t.reverse()
    if len(bin) % 2 == 0: bin = bin [len(bin)/2:]
    else: bin = bin[len(bin)/2 + 1:]
    return t == bin

def palin(n): # decimal input
    return dec_palin(n) and bin_palin(n)


sum = 0
i = 1
while i < 1000000:
    if palin(i): sum += i
    i += 1

print sum

# you don't have to reverse(len(num)), because just reversing it
# will check if it's a palindrome or not....

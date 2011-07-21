#!/usr/bin/env python

def prime(n):
	f = open('small_prime', 'r')
    	a = f.read()
    	a = a.split()
    	for i in a:
		if str(n) == i: return True
    	return False
    	f.close()

def test(i, j):
    count = 0
    n = 0
    while True:
        if not prime(n**2 + i*n + j): return count
	count += 1
        n += 1

def main():
	li = []
	f = open('small_prime', 'r')
	a = f.read()
	li = [int(x) for x in a.split()]
	li = li[:168]
	li += [-1*x for x in li]

	x, y, t, max = 0, 0, 0, 0
	i = -999
	for i in li:
		for j in li:
			t = test(i, j)
        		if t > max: 
				max = t
        			x, y = i, j

	print x, y, max

if __name__ == "__main__":
	main()

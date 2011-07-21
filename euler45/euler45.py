#!/usr/bin/env python

def tri(n):
	return n*(n+1)/2

def pent(n):
	return n*(3*n-1)/2

def hex(n):
	return n*(2*n-1)

def main():
	t, p, h = 286, 2, 2
	while(1):
		if tri(t) == pent(p) and pent(p) == hex(h):
			print tri(t)
			return
		elif tri(t) > pent(p):
			if pent(p) > hex(h):
				h += 1
			else:
				p += 1
		else:
			t += 1
	return	

	

if __name__ == "__main__":
	main()

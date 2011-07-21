#!/usr/bin/env python

def max_sum(tree_arr):
	while len(tree_arr) > 1:
		reduce(tree_arr)
	return tree_arr[0][0]

def reduce(tree_arr):
	last_row = tree_arr[-1]
	for i in xrange(len(tree_arr) - 1):
		tree_arr[-2][i] += max(last_row[i:i+2])
	del tree_arr[-1]

def main():
	tree_arr = []
	f = open('euler67.num', 'r')
	for line in f:
		tree_arr.append([int(x) for x in line.split()])

	print max_sum(tree_arr)

if __name__ == "__main__":
	main()

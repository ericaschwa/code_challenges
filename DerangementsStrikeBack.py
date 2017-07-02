"""
DerangementsStrikeBack
By: Erica Schwartz (ericaschwa)
Solves problem as articulated here:
https://community.topcoder.com/stat?c=problem_statement&pm=14563&rd=16932

Problem Statement:

You are given two ints: n and m.

Let D[i] be the number of permutations of the set {1,2,...,n+i} such that the
first i values are not fixed points of the permutation. Formally, we are
interested in permutations p such that for each j between 1 and i, inclusive,
we have p(j) != j.

Next, let B[i] = (D[i] / n!) modulo (10^9 + 7). Note that it can be shown that
D[i] divided by n! is always an integer.

Compute and return the bitwise xor of the values B[i] for i between 1 and m,
inclusive.
"""

import math

def bitwise_xor(x, y):
	""" Returns the bitwise xor of x and y """
	power  = 0
	result = 0
	while x > 0 or y > 0:
		x_digit = x % 2
		y_digit = y % 2
		if (x_digit == 1 and y_digit == 0) or (x_digit == 0 and y_digit == 1):
			result += pow(2, power)
		power  += 1
		x /= 2
		y /= 2
	return result

def generate_perms(l):
	"""
	Returns list containing all permutations of the given list l
	"""
	if len(l) <= 1: return [l]
	first  = l[0]
	rests  = generate_perms(l[1:])
	result = []
	for rest in rests:
		result += [rest[:i] + [first] + rest[i:] for i in xrange(len(rest) + 1)]
	return result

def num_perms(i, n):
	"""
	Returns the number of permutations of the set {1,2,...,n+i} such that the
	first i values are not fixed points of the permutation
	"""
	perms = generate_perms(range(1, n + i + 1))
	count = 0
	for perm in perms:
		fixed_pt = True
		for j in xrange(1, i):
			if perm[j] == j:
				fixed_pt = False
				break
		if fixed_pt: count += 1
	return count

def count(n, m):
	"""
	Executes the solution to the problem described in the problem statement
	"""
	D = [num_perms(i, n) for i in xrange(1, m + 1)]
	B = [(D[i] / math.factorial(n)) % (pow(10,9) + 7) for i in xrange(len(D))]
	result = B[0]
	for i in xrange(1, len(B)):
		result = bitwise_xor(result, B[i])
	return result

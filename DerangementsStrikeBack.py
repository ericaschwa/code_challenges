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

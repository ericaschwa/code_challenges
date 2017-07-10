"""
PowerEquation
By: Erica Schwartz (ericaschwa)
Solves problem as articulated here:
https://community.topcoder.com/stat?c=problem_statement&pm=14573&rd=16882

Problem Statement:

Fox Ciel is learning about exponentiation. While doing so, she has noticed some
cute identities such as 9^3 = 27^2 and 2^10 = 32^2. 

You are given an int n. Fox Ciel is going to write down all identities of the
form a^b = c^d where 1 <= a,b,c,d <= n. 

Let X be the number of such identities. Compute and return the value
(X modulo (10^9 + 7)).
"""

import copy

def combos_from(n, pow_dict, last_n):
    """
    Returns the number of different power equations involving n and the
    numbers below n
    """
    total = set([(1, n, 1, y) for y in xrange(1, n)] + [(1, y, 1, n) for y in xrange(1, n)])
    total = total.union(set([(n, y, n, y) for y in xrange(1, n)]))
    total = total.union(set([(y, n, y, n) for y in xrange(1, n + 1)]))
    # 2n - 2 + n - 1 + n = 4n - 3

    for i in xrange(2, n):
        for power in xrange(2, last_n):
            i_to_power = pow(i, power)
            if n == i_to_power:  # n is a power of something less than it (i)
                if i not in pow_dict:
                    pow_dict[i] = set()
                for p, num in pow_dict[i]:
                    total = total.union(set([(n, p * j, num, power * j) for j in xrange(1, last_n / power + 1)]))
                    total = total.union(set([(num, power * j, n, p * j) for j in xrange(1, last_n / power + 1)]))
                pow_dict[i].add((power, n))
                total = total.union(set([(n, j, i, power * j) for j in xrange(1, last_n / power + 1)]))
                total = total.union(set([(i, power * j, n, j) for j in xrange(1, last_n / power + 1)]))
                break
            elif n < i_to_power:
                break

    # show that each item in the set is indeed correct
    for a, b, c, d in total:
        assert (a <= last_n and b <= last_n and c <= last_n and d <= last_n)
        assert (a >= 0 and b >= 0 and c >= 0 and d >= 0)
        assert (pow(a, b) == pow(c, d))
    return len(total)

def count(n):
    """
    Executes the solution to the problem described in the problem statement
    """
    pow_dict = {}
    result   = 0
    for i in xrange(1, n + 1):
        result += combos_from(i, pow_dict, n)
    return result % (pow(10, 9) + 7)

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

def combos_from(n, pow_dict, last_n):
    """
    Returns the number of different power equations involving n and the
    numbers below n
    """
    total  = 4 * n - 3
    # 1 ^ n == 1 ^ y and 1 ^ y == 1 ^ n for 0 < y < n (so n - 1), * 2
    # n ^ y == n ^ y for 0 < y < n     (so n - 1)
    # y ^ n == y ^ n for 0 < y < n + 1 (so n)
    # 2n - 2 + n - 1 + n = 4n - 3

    for i in xrange(2, n):
        # n is a power of something less than it (i)
        for power in xrange(2, n):
            i_to_power = pow(i, power)
            if n == i_to_power:
                if i not in pow_dict:
                    pow_dict[i] = []
                for p, num in pow_dict[i]:
                	total += 2 * (last_n / p)
                pow_dict[i].append((power, n))
                total += 2
                break
            elif n < i_to_power:
                break

    return total

def count(n):
    """
    Executes the solution to the problem described in the problem statement
    """
    pow_dict = {}
    result   = 0
    for i in xrange(1, n + 1):
        result += combos_from(i, pow_dict, n)
    return result % (pow(10, 9) + 7)

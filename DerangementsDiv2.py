"""
DerangementsDiv2
By: Erica Schwartz (ericaschwa)
Solves problem as articulated here:
https://community.topcoder.com/stat?c=problem_statement&pm=14632&rd=16932

Problem Statement:

You are given two ints: n and m.

Let D be the number of permutations of the set {1,2,...,n+m} such that the
first m values are not fixed points of the permutation. Formally, we are
interested in permutations p such that for each j between 1 and m, inclusive,
we have p(j) != j.

Compute and return D modulo 1,000,000,007.
"""

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

def num_perms(n, m):
    """
    Returns the number of permutations of the set {1,2,...,n+m} such that the
    first m values are not fixed points of the permutation
    """
    perms = generate_perms(range(1, n + m + 1))
    count = 0
    for perm in perms:
        fixed_pt = True
        for j in xrange(m):
            if perm[j] == j + 1:
                fixed_pt = False
                break
        if fixed_pt: count += 1
    return count

def count(n, m):
    """
    Executes the solution to the problem described in the problem statement
    """
    return num_perms(n, m) % 1000000007

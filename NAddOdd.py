"""
NAddOdd
By: Erica Schwartz (ericaschwa)
Solves problem as articulated here:
https://community.topcoder.com/stat?c=problem_statement&pm=14408&rd=16883

Problem Statement:

The Collatz conjecture (also known as the 3n+1 conjecture) is a well-known open
problem in mathematics. In this problem we'll study a related problem: the
n+odd problem.

You are given an odd int K. The function f is defined as follows: if N is even,
f(N) = N/2, otherwise f(N) = N+K.

For any starting positive integer x, consider the following sequence:
x, f(x), f(f(x)), f(f(f(x))), ...

It can be shown that regardless of x and K the sequence will eventually reach a
value that is less than or equal to K. Let g(x) be the smallest number of
consecutive applications of the function f needed for this to happen.

For example, g(x) = 3 means that the values x, f(x), and f(f(x)) are all
strictly greater than K and the value f(f(f(x))) is at most equal to K.

Another example: Suppose K=1 and x=5. This x defines the following sequence:
5, 5+1 = 6, 6/2 = 3, 3+1 = 4, 4/2 = 2, 2/2 = 1, ...
Hence, in this case we have g(5) = 5.

You are given two longs L and R, and the int K mentioned above. Compute and
return the sum of g(x) for x between L and R, inclusive.
"""

def g(x, k):
    """
    Implements the function g as described in the problem statement
    """
    i = 0
    while x > k:
        i += 1
        if x % 2 == 0: x /= 2
        else         : x += k
    return i

def solve(L, R, k):
    """
    Executes the solution to the problem described in the problem statement
    """
    result = 0
    for x in xrange(L, R + 1):
        result += g(x, k)
    return result

"""
RangeEncoding
By: Erica Schwartz (ericaschwa)
Solves problem as articulated here: (although somewhat modified)
https://community.topcoder.com/stat?c=problem_statement&pm=14592&rd=16883

Problem Statement:

You are given a int[] arr that contains a set of positive integers. The
elements in arr are all distinct and they are given in increasing order.

A range is a finite set of consecutive integers. Formally, for any two positive
integers a <= b the range [a,b] is defined to be the set of all integers that
lie between a and b, inclusive. For example, [3,3] = {3} and [4,7] = {4,5,6,7}.

You want to represent the set given in arr as a union of some ranges. Return
the minimum number of ranges you need.
"""

def min_ranges(l):
    """
    Executes the solution to the problem described in the problem statement
    """
    if len(l) == 0: return 0
    num_ranges = 1
    curr_end   = l[0]
    for i in xrange(1, len(l)):
        if l[i] != curr_end + 1:
        	num_ranges += 1
        curr_end = l[i]
    return num_ranges

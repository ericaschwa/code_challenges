"""
NiceTable
By: Erica Schwartz (ericaschwa)
Solves problem as articulated here:
https://community.topcoder.com/stat?c=problem_statement&pm=14630&rd=16932

Problem Statement:

You are given a String[] t that describes a rectangular table of zeroes and
ones. Each character in t is either '0' or '1'.

We say that a table is nice if there are two sequences x, y of zeroes and ones
such that for each valid pair of indices i, j we have t[i][j] = x[i] xor y[j].

Some technical remarks:

The number of elements in x should be equal to the number of rows of the table,
i.e., the number of elements in t.

The number of elements in y should be equal to the number of columns of the
table, i.e., the length of each string in t.

The operation xor (exclusive or) is defined as follows: 0 xor 0 = 0,
1 xor 1 = 0, 0 xor 1 = 1, and 1 xor 0 = 1.

Verify whether the given table is nice. Return "Nice" if it is nice and
"Not nice" otherwise. Note that the return value is case-sensitive.
"""

def xor(x, y):
    """ Returns x xor y, as defined in the problem statement """
    if x == 1 and y == 0: return 1
    if x == 0 and y == 1: return 1
    if x == 0 and y == 0: return 0
    if x == 1 and y == 1: return 0

def generate_poss_lists(n):
    """
    Given an int, generates all possible lists of 0's and 1's of that length
    """
    if n  == 1: return [[0], [1]]
    l      = generate_poss_lists(n - 1)
    double = []
    for i in xrange(len(l)):
        double.append([0] + l[i])
        l[i] = [1] + l[i]
    return l + double    

def is_nice(t):
    """
    Executes the solution to the problem described in the problem statement
    """
    # generate A from input, as well as list of all possible x and y sequences
    A = []
    for string in t:
        row = []
        for char in string:
            row.append(int(char))
        A.append(row)
    xs = generate_poss_lists(len(A   ))
    ys = generate_poss_lists(len(A[0]))

    # check all x and y sequences to see if any make A nice
    for x in xs:
        for y in ys:
            nice = True
            for i in xrange(len(x)):
                for j in xrange(len(y)):
                    if A[i][j] != xor(x[i], y[j]):
                        nice = False
                        break
                    if not nice: break
            if nice: return "Nice"

    return "not Nice"

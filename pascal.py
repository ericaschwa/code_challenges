"""
pascal
By: Erica Schwartz (ericaschwa)
Solves problem as articulated here:
https://ryanstutorials.net/programming-challenges/

Problem Statement:

Write a program which will print out a Pascal triangle.
"""

# from here:
# https://stackoverflow.com/questions/4941753/is-there-a-math-ncr-function-in-python
import operator as op
def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return numer//denom

def center_print(row, largest_row_size):
    """
    Given a row of pascal's triangle, prints it so that it's centered
    """
    row_size = len(row)
    offset = largest_row_size - row_size
    print "\t" * offset + "\t\t".join(row)

def pascal(n_rows):
    """
    Executes the solution to the problem described in the problem statement
    """
    for n in xrange(n_rows + 1):
        row  = []
        for k in xrange(n + 1):
            row.append(str(ncr(n, k)))
        center_print(row, n_rows + 1)


"""
ConstructLCS
By: Erica Schwartz (ericaschwa)
Solves problem as articulated here: (although somewhat modified)
https://community.topcoder.com/stat?c=problem_statement&pm=14623&rd=16931

Problem Statement:

A string S is a subsequence of a string T if we can obtain S from T by erasing
some (possibly all or none) of its characters. For example, "000" is a
subsequence of "01010".

The longest common subsequence (LCS) of two strings A and B is a string C that
is a subsequence of each of them and has the largest length among all strings
with this property. Let f(A,B) be the length of the LCS of strings A and B. For
example, we have f("101", "111000") = 2, f("101", "110011") = 3, and
f("00", "1111") = 0. 

You are given two strings A and B. Please find their LCS.
"""

def LCS_DP(L, A, B, m, n):
    """
    Fills in the DP matrix for finding the LCS
    """
    for i in xrange(1, m+1):
        for j in xrange(1, n+1):
            add = 0
            if A[i-1] == B[j-1]: add = 1
            up   = L[i-1][j][0]
            left = L[i]  [j-1][0]
            diag = L[i-1][j-1][0] + add
            if   up   > left and up   > diag: L[i][j] = (up,   0, 0)
            elif left > up   and left > diag: L[i][j] = (left, 1, 0)
            else                            : L[i][j] = (diag, 2, add)

def retrace_matrix(L, A, m, n):
    """
    Retraces the DP matrix to find the LCS
    """
    lcs_reverse  = ""
    x            = n
    y            = m
    while x > 0 or y > 0:
        curr = L[y][x]
        if curr[1] == 2 and curr[2] == 1:
            lcs_reverse += A[y-1]
            x -= 1
            y -= 1
        elif curr[1] == 1:
            x -= 1
        else:
            y -= 1
    lcs = ""
    for i in xrange(len(lcs_reverse) - 1, -1, -1):
        lcs += lcs_reverse[i]
    return lcs


def LCS(A, B):
    """
    Executes the solution to the problem described in the problem statement
    """
    m = len(A)
    n = len(B)
    L = [[None]*(n+1) for i in xrange(m+1)]
    for i in xrange(m+1):
        L[i][0] = (0, 0, 0)
    for i in xrange(n+1):
        L[0][i] = (0, 1, 0)
    LCS_DP        (L, A, B, m, n)
    return retrace_matrix(L, A,    m, n)

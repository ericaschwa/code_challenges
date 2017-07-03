"""
LexmaxReplace
By: Erica Schwartz (ericaschwa)
Solves problem as articulated here:
https://community.topcoder.com/stat?c=problem_statement&pm=14631&rd=16932

Problem Statement:

Alice has a string s of lowercase letters. The string is written on a wall.

Alice also has a set of cards. Each card contains a single letter. Alice can
take any card and glue it on top of one of the letters of s. She may use any
subset of cards in this way, possibly none or all of them. She is not allowed
to glue new letters in front of s or after s, she can only replace the existing
letters.

Alice wants to produce the lexicographically largest possible string.

You are given the String s. You are also given a String t. Each character of t
is a letter written on one of the cards. Compute and return the
lexicographically largest string Alice can produce on the wall while following
the rules described above.
"""

def get(s, t):
    """
    Executes the solution to the problem described in the problem statement
    """
    x = list(t)
    y = list(s)
    x.sort()
    for i in xrange(len(y)):
    	if len(x) == 0: break
        if  y[i] < x[-1]:
            y[i] = x.pop()
    return "".join(y)
            
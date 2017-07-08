"""
RemovingParenthesis
By: Erica Schwartz (ericaschwa)
Solves problem as articulated here:
https://community.topcoder.com/stat?c=problem_statement&pm=14593&rd=16883

Problem Statement:

Correct parentheses sequences can be defined recursively as follows:

The empty string "" is a correct sequence.
If "X" and "Y" are correct sequences, then "XY" (the concatenation of X and Y)
is a correct sequence.
If "X" is a correct sequence, then "(X)" is a correct sequence.
Each correct parentheses sequence can be derived using the above rules.
Examples of correct parentheses sequences include "", "()", "()()()", "(()())",
and "(((())))".

You are given a String s that is guaranteed to be a correct parentheses
sequence. A removal is an action that consists of two steps:

Remove the first opening parenthesis in s.
Remove one closing parenthesis in s. After you do so, s must again be a correct
parentheses sequence.
Compute and return the number of distinct ways in which s can be reduced to an
empty string by performing consecutive removals. Two ways are considered
distinct if there is a step in which you remove a different closing
parenthesis. (See Example 1 for clarification.) It is guaranteed that the
correct return value will always fit into a 32-bit signed integer.
"""

def correct_parenthesis(s):
    """
    Returns true if parenthesis are correct, false otherwise
    """
    stack = []
    for c in s:
        if c == '(': stack.append(c)
        elif len(stack) == 0: return False
        else: stack.pop()
    return True

def count_ways(s):
    """
    Executes the solution to the problem described in the problem statement
    """
    if len(s)   == 0: return 1
    result = 0
    for i in xrange(1, len(s)):
        if s[i] == ')':
            substr = s[1:i] + s[i+1:]
            if correct_parenthesis(substr):
                result += count_ways(substr)
    return result

"""
MaximumRange
By: Erica Schwartz (ericaschwa)
Solves problem as articulated here:
https://community.topcoder.com/stat?c=problem_statement&pm=14613&rd=16884

Problem Statement:

Cat Noku was given a calculator for his birthday. The calculator is very
simple. It can only store a single variable. The variable is called X and its
initial value is 0. The calculator has only two buttons: + and -. Pressing +
increments X by 1 and pressing - decrements X by 1. For example, if X is 4 and
Noku presses +, X is incremented to 5.

A string of '+' and '-' characters can be seen as a sequence of instructions to
press the corresponding buttons. The range of such a sequence of instructions
is the difference between the largest and the smallest value stored in X while
executing that sequence of instructions, in order.

For example, the range of "+++++++" is 7: the largest value of X is 7 (at the
end) and the smallest value is 0 (in the beginning). The range of "---" is 3:
maximum is 0, minimum is (-3), their difference is 0 - (-3) = 3. The range of
"+-+-+-" is 1. The range of an empty sequence of instructions is 0.

Noku's calculator came with a piece of paper that contained a String s. Each
character of s was either '+' or '-'. Noku will choose and execute any (not
necessarily contiguous) subsequence of these characters. Help him do so in a
way that maximizes the range of the executed sequence.

Compute and return the maximal range of a subsequence of the String s.
"""

def generate_substrings(s):
    """
    Generates and returns all substrings of the string s
    """
    if len(s) == 0: return [s]
    result = []
    for i in xrange(len(s)):
        result += generate_substrings(s[:i] + s[i+1:])
    return [s] + result

def score(s):
    """
    Given a string of +'s and -'s, scores it and returns its max range
    """
    largest_x = smallest_x = x = 0
    for c in s:
        if   c == '-':
            x -= 1
            if x < smallest_x: smallest_x = x
        elif c == '+':
            x += 1
            if x > largest_x: largest_x = x
    return largest_x - smallest_x

def find_max(s):
    """
    Executes the solution to the problem described in the problem statement
    """
    substrings    = set(generate_substrings(s))
    max_s         = -1
    for substring in substrings:
        s = score(substring)
        if s > max_s: max_s = s
    return max_s


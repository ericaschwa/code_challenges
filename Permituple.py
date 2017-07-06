"""
Permituple
By: Erica Schwartz (ericaschwa)
Solves problem as articulated here:
https://community.topcoder.com/stat?c=problem_statement&pm=14628&rd=16931

Problem Statement:

You are given a positive integer x. Please check whether we can rearrange the
digits of x (in base 10, without leading zeros) to produce a different number
that is a multiple of x. 

Return "Possible" if this can be done and "Impossible" otherwise. Note that
the return value is case-sensitive.
"""

def get_digs(x):
    """
    Given a number, returns its digits as a list
    """
    result_reverse = []
    while x > 0:
        result_reverse.append(x % 10)
        x /= 10
    result = []
    while len(result_reverse) > 0:
        result.append(result_reverse.pop())
    return result

def get_num(l):
    """
    Given a list of digits, return the number
    """
    num = 0
    i   = 0
    while len(l) > 0:
        digit = l.pop()
        num += digit * pow(10, i)
        i   += 1
    return num

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

def is_possible(x):
    """
    Executes the solution to the problem described in the problem statement
    """
    digits             = get_digs(x)
    digit_arrangements = generate_perms(digits)
    for digit_arrangement in digit_arrangements:
        number         = get_num(digit_arrangement)
        if number == x: continue
        if number % x == 0: return "Possible"
    return "Impossible"

"""
Saleswoman
By: Erica Schwartz (ericaschwa)
Solves problem as articulated here:
https://community.topcoder.com/stat?c=problem_statement&pm=14120&rd=16883

Problem Statement:
        
There are n people who live on the real axis. The people are numbered 0 through
n-1. Person i lives at the position pos[i]. All of the positions are distinct.

Alice is a saleswoman. She travels along the real axis and makes trades with
the n people who live there. Alice trades items of a single type. Each person has
a particular supply or demand of that item. In particular, if delta[i] is
positive, the person has a supply of delta[i] units, otherwise the person has a
demand of -delta[i] units. It is guaranteed that the sum of all elements of
delta is nonnegative.

At the beginning, Alice is at position 0 and she has no items. In one second,
she can move left or right by one unit. She can trade with a person if and only
if she is exactly at the same position as that person. All trades happen
instantly. During each trade Bob can buy or sell as many items as he wants. Of
course, she can only sell the items she currently owns. While walking along the
real axis, Alice can carry arbitrarily many items at the same time. She can
pass through a position with a person without trading with them, if that is
what she wants. (She can always come back and trade with them later.)

Alice has two goals:
She must trade the items in a way that will satisfy all demands.
She must end her travels at the position of the rightmost person.
Determine and return the smallest amount of time in which Alice can achieve
both goals.
"""

import math

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

def min_moves(positions, supplies):
    """
    Executes the solution to the problem described in the problem statement
    """
    total_demand  = -1 * sum([x for x in supplies if x < 0])
    rightmost     = positions[-1]
    supply_dict   = {positions[i]: supplies[i]  for i in xrange(len(supplies))}
    poss_seqs     = generate_perms(positions)
    minimum       = float('inf')
    for seq in poss_seqs:
        seq.append(rightmost)
        num_steps = curr_pos = supply = 0
        demand    = total_demand
        for spot in seq:
            num_steps += math.fabs(curr_pos - spot)
            curr_pos   = spot
            if demand <= 0: break
            if supply_dict[spot] >= 0:             # buy their wares
                supply += supply_dict[spot]
            elif supply >= supply_dict[spot] * -1: # fill their supply
                supply += supply_dict[spot]
                demand += supply_dict[spot]
            else: num_steps = float('inf')         # can't fill wares, skip it
        if num_steps < minimum:
            minimum = num_steps
    return int(minimum)



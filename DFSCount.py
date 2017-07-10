"""
DFSCount
By: Erica Schwartz (ericaschwa)
Solves problem as articulated here:
https://community.topcoder.com/stat?c=problem_statement&pm=14588&rd=16882

Problem Statement:
Fox Ciel has a simple undirected graph with n vertices. The vertices are
numbered 0 through n-1. The graph is connected.

You are given a String[] G containing the adjacency matrix of the graph. More
precisely, for each i and j, G[i][j] is 'Y' if there is an edge between
vertices i and j and it is 'N' if there is no such edge. 

Ciel then implemented a depth-first search: 

p = []

[ "NYY","YNY","YYN"]
 6

[ "NYNN","YNYN","NYNY","NNYN"]
 6 !!

[ "NYYY","YNYY","YYNN","YYNN"]
 16 !!

[ "N"]
 1

dfs(current) := 
    p.append(current)
    Let adjs[] = list of vertices that are adjacent to current.
    random_shuffle(adjs)
    for v in adjs:
        if v is not in p:
            dfs(v)

Let start = random(0, n-1)   # a random number between 0 and n-1, inclusive
dfs(start)
output(p)

Clearly, the output of this algorithm is always a permutation of the numbers
from 0 to n-1. However, as the algorithm uses randomness, there may be multiple
possible outputs. Please compute and return the number of different
permutations the algorithm may return.
"""

def all_perms(l):
    """
    Returns list containing all permutations of the given list l
    """
    if len(l) <= 1: return [l]
    first  = l[0]
    rests  = all_perms(l[1:])
    result = []
    for rest in rests:
        result += [rest[:i] + [first] + rest[i:] for i in xrange(len(rest) + 1)]
    return result

def dfs(i, adj_lists, order, index, marks):
    """
    Returns one way to do a DFS from index i given
    the graph and the already-visited vertices
    """
    marks[i] = True
    poss_dfs = []
    next_i   = order[index]
    for neighbor in adj_lists[i][next_i % len(adj_lists[i])]:
        if not marks[neighbor]:
            way = dfs(neighbor, adj_lists, order, index + 1, marks)
            poss_dfs += way
    return [i] + poss_dfs

def count(adj_s):
    """
    Executes the solution to the problem described in the problem statement
    """
    adj_lists  = {
        i: all_perms([j for j in xrange(len(adj_s[i])) if adj_s[i][j] == 'Y'])
                        for i in xrange(len(adj_s))
    }
    list_orders = all_perms(range(len(adj_s))) # TODO: allow repetition
    paths = set()
    for i in adj_lists:
        for order in list_orders:
            marks     = [False for j in xrange(len(adj_lists))]
            new_paths = dfs(i, adj_lists, order, 0, marks)
        paths.add(tuple(new_paths))
    print paths
    return len(paths)








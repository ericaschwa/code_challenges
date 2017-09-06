"""
pageRank
By: Erica Schwartz (ericaschwa)
Implements algorithm as articulated here:
https://en.wikipedia.org/wiki/PageRank#Algorithm
"""

def rank(adj_map):
    """
    Executes the solution to the problem described in the problem statement
    """
    # reverse adj_map so you have a map from nodes to all nodes that
    # point to them
    rev_map = {node : [] for node in adj_map}
    for node in adj_map:
        for neighbor in adj_map[node]:
            rev_map[neighbor].append(node)

    # initialize N, scores, and dampening factor
    N      = float(len(rev_map))
    scores = {node : 1.0/N for node in rev_map}
    d      = 0.85

    # iterate until somewhat stable
    done = False
    while not done:
        done = True
        for node in rev_map:
            old_score    = scores[node]
            weighted_sum = sum([scores[neighbor] / len(adj_map[neighbor])
                                for neighbor in rev_map[node]])
            scores[node] = (1 - d) / N + d * weighted_sum
            if (old_score - scores[node]) / float(old_score) >  0.0001 or \
               (old_score - scores[node]) / float(old_score) < -0.0001:
                done = False

    return scores


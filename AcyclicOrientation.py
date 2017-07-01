"""
AcyclicOrientation
By: Erica Schwartz (ericaschwa)
Solves problem as articulated here:
https://community.topcoder.com/stat?c=problem_statement&pm=14598&rd=16932

Problem Statement:

You are given a simple undirected graph G on n vertices. The vertices are
numbered 0 through n-1. You are given the int n and two int[]s u and v that
contain the list of edges. More precisely, for each valid index i the graph
contains an edge between the vertices u[i] and v[i].

An orientation of G is a directed graph that can be obtained from G by
assigning one of the two possible directions to each edge of G. Let A(G) be the
number of orientations of G that are acyclic. Compute and return the value A(G)
modulo 6.
"""

def is_acyclic(adj_mtx):
	"""
	Given an adjacency matrix, returns True if its graph is acyclic and False
	otherwise
	""" 
	n       = len(adj_mtx)
	visited = set()
	for start in xrange(n):
		if start in visited: continue
		visited_edges = set()
		stack         = [start]
		while len(stack) > 0:
			curr        = stack.pop()
			visited.add(curr)
			for i in xrange(n):
				if adj_mtx[curr][i]:
					if (curr, i) in visited_edges:
						return False
					visited_edges.add((curr, i))
					stack.append(i)
	return True
		
def uv_to_adj_mtx(n, u, v):
	"""
	Given u and v as specified in the problem statement, returns the
	corresponding adjacency matrix
	"""
	m = [[False for i in xrange(n)] for j in xrange(n)]
	for i in xrange(len(u)):
		m[u[i]][v[i]] = True
	return m

def rearrange_to_directed(directions, u, v):
	"""
	Given u and v as specified in the problem statement, and the
	direction of each edge represented by a list of Booleans, returns
	the directed edges in (u, v) format
	"""
	new_u = []
	new_v = []
	for i in xrange(len(u)):
		if directions[i]:
			new_u.append(u[i])
			new_v.append(v[i])
		else:
			new_u.append(v[i])
			new_v.append(u[i])
	return (new_u, new_v)

def generate_poss_directions(n):
	"""
	Given the number of edges, returns a list of all possible orientations of
	the graph, each represented by a list of edge directions.
	"""
	if n  == 1: return [[True], [False]]
	l      = generate_poss_directions(n - 1)
	double = []
	for i in xrange(len(l)):
		double.append([True] + l[i])
		l[i] = [False] + l[i]
	return l + double	

def count(n, u, v):
	"""
	Executes the solution to the problem described in the problem statement
	"""
	if len(u) == 0: return 1
	permutations = generate_poss_directions(len(u))
	count = 0
	for p in permutations:
		new_u, new_v = rearrange_to_directed(p, u, v)
		adj_mtx      = uv_to_adj_mtx(n, new_u, new_v)
		if is_acyclic(adj_mtx):
			count += 1
	return count % 6


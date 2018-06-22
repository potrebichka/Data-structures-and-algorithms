#Uses python2

import sys
import threading

# This code is used to avoid stack overflow issues
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**26)  # new thread will get stack of such size
 
def toposort_node(node, adj, visited, order):
    global result
    #mark the current node as visited
    visited[node] = True
    for i in adj[node]:
        if not visited[i]:
            if adj[node] == []:
                result += 1
            toposort_node(i, adj, visited, order)
    order.append(node+1)
	
def toposort(adj):
    global result
    # mark all nodes as unvisited
    visited = [False] * len(adj)
    # lisr of order of nodes
    order = []
    result = 0
    # recursive function for all nodes
    for i in range(len(adj)):
        # check whether the node is unvisited
        if not visited[i]:
            toposort_node(i, adj, visited, order)
    return list(reversed(order))


def number_of_strongly_connected_components(adj):
    global result
    #topological sorting
    order = toposort(adj)
    result = 0
    # mark all nodes as unvisited
    visited = [False] * len(adj)
    # lisr of order of nodes
    #order = []
    
    # recursive function for all nodes
    for i in order:
        # check whether the node is unvisited
        if not visited[i-1]:
            toposort_node(i-1, reversed_adj, visited, order)
            # mark new visited nodes as SSC
            result += 1
    return result

n, m = list(map(int, raw_input().split()))
edges = []
for i in range(m):
    a, b = map(int, raw_input().split())
    edges.append((a, b))

adj = [[] for _ in range(n)]
reversed_adj = [[] for _ in range(n)]
for (a, b) in edges:
    adj[a - 1].append(b - 1)
    reversed_adj[b-1].append(a-1)

print(number_of_strongly_connected_components(adj))    
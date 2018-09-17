#Uses python2
# Given an directed graph with possibly negative edge weights and with n vertices and m edges as well
#as its vertex s, compute the length of shortest paths from s to all other vertices of the graph.

# For all vertices i from 1 to n output the following on a separate line:
# "*", if there is no path from s to u;
# "-", if there is a path from s to u, but there is no shortest path from s to u (that is, the distance
#from s to u is -infinity);
# the length of a shortest path otherwise.

import sys
#import queue


def BellmanFord(adj, dist):
    # no negative cycles in G
    changed = False
    A = set()
    for u in range(len(adj)):
        i = 0
        for v in adj[u]:
            #relax nodes
            if dist[v] > dist[u] + cost[u][i]:
                dist[v] = dist[u] + cost[u][i]
                changed = True
                A.add(u)
                A.add(v)
            i += 1
    return changed, A    


def shortest_paths(adj, cost, s, distance, reachable, shortest):
    #write your code here
    distance[s] = 0
    # do n-1 times a BellmanFord
    for _ in range(n-1):
        BellmanFord(adj, distance)
    # check if there are any negative cycles    
    changed, A = BellmanFord(adj, distance)
    if changed:
        for node in A:
            shortest[node] = 0
    '''
    distance = [float("inf")] * n       
    distance[s] = 0
    BellmanFord(adj, distance)'''
    # breadth search for connected nodes through negative cycles
    visited = [False] * n  
    B = set()
    for node in A:
        bfs(adj, node, visited, B)
    
    for node in B:
        shortest[node] = 0
    
    # find all reachable nodes from source node
    R = set()
    visited = [False] * n
    bfs(adj, s, visited, R)
    for node in R:
        reachable[node] = 1
        
def bfs(adj, s, visited, B):
    visited[s] = True
    B.add(s)
    for vertex in adj[s]:
        if not visited[vertex]:
            bfs(adj, vertex, visited, B)
    return B


n, m = list(map(int, raw_input().split()))

edges = []
for i in range(m):
    a, b, w = map(int, raw_input().split())
    edges.append(((a, b), w))

adj = [[] for _ in range(n)]
cost = [[] for _ in range(n)]

for ((a, b), w) in edges:
    adj[a - 1].append(b - 1)
    cost[a - 1].append(w)

s = int(raw_input())
s -= 1
distance = [float("inf")] * n
reachable = [0] * n
shortest = [1] * n
shortest_paths(adj, cost, s, distance, reachable, shortest)
for x in range(n):
    if reachable[x] == 0:
        print('*')
    elif shortest[x] == 0:
        print('-')
    else:
        print(distance[x])

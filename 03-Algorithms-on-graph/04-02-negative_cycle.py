#### Uses python2

import sys

def Relax(u, v, dist, cost):
    if dist[v] > dist[u] + cost:
        dist[v] = dist[u] + cost
    return dist

def BellmanFord(adj):
    # no negative cycles in G
    global dist
    changed = False
    # repeat n times
    for u in range(len(adj)):
        i = 0
        for v in adj[u]:
            if dist[v] > dist[u] + cost[u][i]:
                dist[v] = dist[u] + cost[u][i]
                changed = True
            if dist[u] == float("inf") and dist[v] != float("inf"):
                dist[u] = dist[v] - cost[u][i]
            i += 1
    return changed 

def negative_cycle(adj, cost):
    #write your code here
    global dist
    dist = [float("inf") for _ in range(len(adj))]
    """    
    for i in range(len(adj)):
        dist.append(float(0))
	"""
    dist[0] = 0
    for _ in range(n-1):
        BellmanFord(adj)
    cycle = BellmanFord(adj)
	
    return 1 if cycle else 0

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
print(negative_cycle(adj, cost))
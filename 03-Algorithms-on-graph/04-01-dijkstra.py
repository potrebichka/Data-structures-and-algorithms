#Uses python2

import sys
#import queue


def distance(adj, cost, s, t):
    #write your code here
    dist = [float("inf") for _ in range(len(adj))]
    prev = [None for _ in range(len(adj))]
    dist[s] = 0
    
    H = dict()
    for i in range(len(adj)):
        H[i] = dist[i]
        
    while len(H) > 0:
        minimum_distance = min(H.itervalues())
        U = [key for key, value in H.iteritems() if value == minimum_distance]
        u = U[0]
        H.pop(u)
        i = 0
        for v in adj[u]:
            if dist[v] > dist[u] + cost[u][i]:
                dist[v] = dist[u] + cost[u][i]
                H[v] = dist[v]
                prev[v] = u
            i += 1
    return -1 if dist[t] == float("inf") else dist[t]


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
    
s, t = list(map(int, raw_input().split()))
s-=1
t-=1
print(distance(adj, cost, s, t))


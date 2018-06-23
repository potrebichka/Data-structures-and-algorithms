#Uses python2

import sys
import Queue

def bipartite(adj):
    #write your code here
    
    color = [float("inf") for _ in range(len(adj))]
    color[0] = 0
    q = Queue.Queue()
    q.put(0)
    while not q.empty():
        u = q.get()
        for v in adj[u]:
            if color[v] == float("inf"):
                q.put(v)
                color[v] = (color[u] + 1) % 2
            elif color[v] == color[u]:
                return 0 
    return 1

n, m = list(map(int, raw_input().split()))

edges = []
for i in range(m):
    a, b = map(int, raw_input().split())
    edges.append((a, b))

adj = [[] for _ in range(n)]
for (a, b) in edges:
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)

print(bipartite(adj))

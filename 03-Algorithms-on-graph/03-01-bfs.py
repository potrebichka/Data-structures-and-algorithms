#### Uses python2

import sys
import Queue 

def distance(adj, s, t):
    #write your code here
	dist = [float("inf") for _ in range(len(adj))]
    dist[s] = 0
    q = Queue.Queue()
    q.put(s)
    while not q.empty():
        u = q.get()
        for v in adj[u]:
            if dist[v] == float("inf"):
                q.put(v)
                dist[v] = dist[u] + 1
    
    return dist[t] if dist[t] != float("inf") else -1


n, m = list(map(int, raw_input().split()))

edges = []
for i in range(m):
    a, b = map(int, raw_input().split())
    edges.append((a, b))

adj = [[] for _ in range(n)]
for (a, b) in edges:
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)

s, t = list(map(int, raw_input().split()))
s-=1
t-=1
print(distance(adj, s, t))


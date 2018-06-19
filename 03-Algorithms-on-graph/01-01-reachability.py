#python2
def reach(adj, u, v):
    global visited
    #result = 0
    #write your code hereve
    visited = [False for _ in range(n)]
    return Explore(adj, u, v)

def Explore(adj, u, v):
    global visited
    visited[u] = True
    if v == u:
        return 1
    for vertex in adj[u]:
        if vertex == v:
            return 1
        else:
            if not visited[vertex]:
                if Explore(adj, vertex, v) == 1:
                    return 1
    if v == u:
        return 1
    return 0

input = raw_input()
n, m = map(int, input.split())
edges = []
for i in range(m):
    a, b = map(int, raw_input().split())
    edges.append((a, b))

adj = [[] for _ in range(n)]
for (a, b) in edges:
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)
u, v = map(int, raw_input().split())
u, v = u-1, v-1
print(reach(adj, u, v))
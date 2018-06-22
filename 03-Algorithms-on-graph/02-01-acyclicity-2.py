
def Explore(vertex, adj, visited, stack):
    visited[vextex] = True
    stack[vertex] = True
    if not adj[vertex]:
        return 0
    
    for new_vertex in range(adj[vertex]):
          if not visited[new_vertex]:
            if Explore(new_vertex, adj, visited, stack) == 1:
                return 1
            elif stack[new_vertex]:
                return 1
    stack[vertex] = False
    return 0
        

def acyclic(adj):
    if adj == []:
        return 0
    visited = [False for _ in range(n)]
    stack = [False for _ in range(n)]
    
    for vertex in range(n):
        if not visited[vertex]:
            if Explore(vertex, adj, visited, stack) == 1:
                return 1
    return 0
        

n, m = list(map(int, raw_input().split()))

edges = []
for i in range(m):
    a, b = map(int, raw_input().split())
    edges.append((a, b))

adj = [[] for _ in range(n)]
for (a, b) in edges:
    adj[a - 1].append(b - 1)

print(acyclic(adj))

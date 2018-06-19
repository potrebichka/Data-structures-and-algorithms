#python2
def connected_components(adj):
    #write your code here
    global visited
    result = 0
    visited = [False for _ in range(n)]
    for i in range(len(adj)):
        if not visited[i]:
            Explore(adj, i)
            result += 1      
    return result

def Explore(adj, u):
    global visited
    visited[u] = True
    for vertex in adj[u]:
        if not visited[vertex]:
            Explore(adj, vertex)

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

print(connected_components(adj))
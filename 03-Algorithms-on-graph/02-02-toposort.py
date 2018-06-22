# python2         
def toposort_node(node, adj, visited, order):
    #mark the current node as visited
    visited[node] = True
    
    for i in adj[node]:
        if not visited[i]:
            toposort_node(i, adj, visited, order)
    order.append(node+1)

def toposort(adj):
    # mark all nodes as unvisited
    visited = [False] * len(adj)
    # lisr of order of nodes
    order = []
    
    # recursive function for all nodes
    for i in range(len(adj)):
        # check whether the node is unvisited
        if not visited[i]:
            toposort_node(i, adj, visited, order)
    return list(reversed(order))

n, m = list(map(int, raw_input().split()))

edges = []
for i in range(m):
    a, b = map(int, raw_input().split())
    edges.append((a, b))

adj = [[] for _ in range(n)]
for (a, b) in edges:
    adj[a - 1].append(b - 1)

order = toposort(adj)
print ' '.join(str(p) for p in order) 


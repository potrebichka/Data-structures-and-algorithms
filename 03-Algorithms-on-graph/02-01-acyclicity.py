#python2
#Check whether a given directed graph with n vertices and m edges contains a cycle

def Explore(vertex, adj, visited, visited_list):
    visited[vertex] = True
    visited_list.append(vertex)
    vertex_new = adj[vertex]
    if vertex_new == []:
        return 0
    if isinstance(vertex_new, list):
        for i in range(len(vertex_new)):
            vertex = vertex_new[i]
            if not visited[vertex]:
                if Explore(vertex, adj, visited, visited_list) == 1:
                    return 1
                else:
                    visited_list.remove(vertex)
            elif vertex in visited_list:
                return 1
        return 0
    else:
        if not visited(vertex):
            if Explore(vertex, adj, visited, visited_list) == 1:
                return 1
            else:
                visited_list.remove(vertex)
        elif vertex in visited_list:
            return 1
    return 0
        

def acyclic(adj):
    if adj == []:
        return 0
    visited = [False for _ in range(n)]
    
    for i in range(n):
        vertex = i
        visited_list = []
        if isinstance(vertex, list):
            for j in range(len(vertex)):
                vertex = vertex[j]
                if not visited[vertex]:
                    if Explore(vertex, adj, visited, visited_list)== 1:
                        return 1
        else:
            if not visited[vertex]:
                if Explore(vertex, adj, visited, visited_list) == 1:
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

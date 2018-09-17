#Uses python2
import sys
import math


def clustering(x, y, k):
    #write your code here
    result = float("inf")
    if k <= 1 or len(x) <= 1:
        return 0.
    #write your code here
    # arrange list of disjoint sets
    MakeSet = list()
    for i in range(n):
        a = set()
        a.add((x[i], y[i]))
        MakeSet.append(a)

    discovered_vertices = set()
    
    # calculating of length of edges
    edges = {}
    
    for i in range(n):
        for j in range(n):
            if i != j and not ((x[j], y[j]), (x[i], y[i])) in edges:
                edge = math.sqrt((x[i] -  x[j])**2 + (y[i] - y[j])**2)
                edges[(x[i], y[i]), (x[j], y[j])] = edge
    if len(edges) == 1:
        return edges.items()[0][1]
    while len(MakeSet) >= k:
        # finding minimum edge and its vertices
        minimum_edge_vertices = min(edges.items(), key=lambda x: x[1])[0]
        
        # processing MakeSet
        remove_list = list()
        y = set()
        y.add(minimum_edge_vertices[0])
        y.add(minimum_edge_vertices[1])
        for element in MakeSet:
            # joining of disjoint sets with corresponding vertices of edge
            intersection_element = y.intersection(element)
            if len(intersection_element) > 0:
                y = y.union(element)
                remove_list.append(element)

        for el in remove_list:
            MakeSet.remove(el)
        MakeSet.append(y)
        
        # add corresponding vertices of minimal edge to set of discovered vertices
        discovered_vertices.add(minimum_edge_vertices[0])
        discovered_vertices.add(minimum_edge_vertices[1])
            
        del edges[minimum_edge_vertices]
    
    result = min(edges.items(), key=lambda x: x[1])[1]
    
    return result


n = int(raw_input())
x = list()
y = list()
for _ in range(n):
    input = raw_input().split()
    x.append(int(input[0]))
    y.append(int(input[1]))
k = int(raw_input())

print("{0:.9f}".format(clustering(x, y, k)))

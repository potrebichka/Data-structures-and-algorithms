#Uses python2
import sys
import math

def minimum_distance(x, y):
    result = 0.
    if len(x) <= 1:
        return result
    #write your code here
    # arrange list of disjoint sets
    MakeSet = list()
    for i in range(n):
        a = set()
        a.add((x[i], y[i]))
        MakeSet.append(a)
    # set of chosen edges
    X = set()
    discovered_vertices = set()
    
    # calculating of length of edges
    edges = {}
    for i in range(n):
        for j in range(n):
            if i != j and not ((x[j], y[j]), (x[i], y[i])) in edges:
                edge = math.sqrt((x[i] -  x[j])**2 + (y[i] - y[j])**2)
                edges[(x[i], y[i]), (x[j], y[j])] = edge

    while True:
        # finding minimum edge and its vertices
        minimum_edge_vertices = min(edges.items(), key=lambda x: x[1])[0]
        
        # processing MakeSet
        remove_list = list()
        y = set()
        y.add(minimum_edge_vertices[0])
        y.add(minimum_edge_vertices[1])
        break_var = False
        for element in MakeSet:
            # checking if it would be a cycle. In this case delete this edge and break the cycle
            if y.issubset(element):
                del edges[minimum_edge_vertices]

                break_var = True
                break
            else:
                # joining of disjoint sets with corresponding vertices of edge
                intersection_element = y.intersection(element)
                if len(intersection_element) > 0:
                    y = y.union(element)
                    remove_list.append(element)
        if break_var:
            continue
        for el in remove_list:
            MakeSet.remove(el)
        MakeSet.append(y)
        
        # add corresponding vertices of minimal edge to set of discovered vertices
        discovered_vertices.add(minimum_edge_vertices[0])
        discovered_vertices.add(minimum_edge_vertices[1])
        
        # updating result
        result += edges[minimum_edge_vertices]
        
        # add corresponding vertices to set of chosen edges
        X.add(minimum_edge_vertices)
        
        # check if we connected all vertices
        if len(MakeSet) == 1:
            break
            
        del edges[minimum_edge_vertices]
    return result


n = int(raw_input())
x = list()
y = list()
for _ in range(n):
    input = raw_input().split()
    x.append(int(input[0]))
    y.append(int(input[1]))
print("{0:.9f}".format(minimum_distance(x, y)))

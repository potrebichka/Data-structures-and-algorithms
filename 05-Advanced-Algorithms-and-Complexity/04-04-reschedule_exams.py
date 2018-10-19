# python2
# reduction to 2-sat algorithm
import itertools

import sys
import threading
global digits_vertices, digits_colors

# This code is used to avoid stack overflow issues
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**26)  # new thread will get stack of such size

# Arguments:
#   * `n` - the number of vertices.
#   * `edges` - list of edges, each edge is a tuple (u, v), 1 <= u, v <= n.
#   * `colors` - list consisting of `n` characters, each belonging to the set {'R', 'G', 'B'}.
# Return value: 
#   * If there exists a proper recoloring, return value is a list containing new colors, similar to the `colors` argument.
#   * Otherwise, return value is None.

def define_clauses(n, edges, colors):
    # cell [i] contains exactly one color
    clauses = []
    
    # color should changed from initial
    for i in range(n):
        if colors[i] == 'R':
            clauses.append([-varnum(i+1, 1)])
            clauses = exactly_one_of_2([varnum(i+1,2), varnum(i+1, 3)], clauses)
        elif colors[i] == 'G':
            clauses.append([-varnum(i+1, 2)])
            clauses = exactly_one_of_2([varnum(i+1,1), varnum(i+1, 3)], clauses)
        elif colors[i] == 'B':
            clauses.append([-varnum(i+1, 3)])
            clauses = exactly_one_of_2([varnum(i+1,1), varnum(i+1, 2)], clauses)
    '''
    for (i) in digits_vertices:
        clauses = exactly_one_of_3([varnum(i, j) for j in digits_colors], clauses)
    '''    
    # edges has different color
    for (i1, i2) in edges:
        for j in digits_colors:
            clauses = one_of_2([varnum(i1,j), varnum(i2,j)], clauses)
    return clauses


def varnum(i, j):
    assert(i in digits_vertices and j in digits_colors)
    return 10*(i) + 1*j


def exactly_one_of_3(literals, clauses):
    clauses.append([l for l in literals])
    for pair in itertools.combinations(literals, 3):
        clauses.append([-l for l in pair])
        clauses.append([-pair[0], -pair[1], pair[2]])
        clauses.append([-pair[0], pair[1], -pair[2]])
        clauses.append([pair[0], -pair[1], -pair[2]])
    return clauses
        
def exactly_one_of_2(literals, clauses):
    clauses.append([-l for l in literals])
    clauses.append([l for l in literals])
    return clauses

def one_of_2(literals, clauses):
    clauses.append([-l for l in literals])
    return clauses


def implication_graph(clauses):
    graph = {}
    for j in range(len(clauses)):
        clause = clauses[j]
        if len(clause) == 2:
            i, j = clause
            if graph.get(-i) == None:
                graph[-i] = []
            
            graph[-i].append(j)

            if graph.get(-j) == None:
                graph[-j] = []
            
            graph[-j].append(i)
        elif(len(clause)) == 1:
            i = clause[0]
            if graph.get(-i) == None:
                graph[-i] = []
            
            graph[-i].append(i)
    return graph

def isSatisfiable(graph, n):
    
    SCC = []
    #tarjan algorithm to find SCCs
    index = [0]
    S = []
    inSCC = {}
    index_list = {}
    lowlink = {}
    onStack = {}

    #result_list = [None]*(2*n)
    result_list = {}
    result= [None]* n
    
        
    def strongconnect(v):
        # set the depth index for v to the smallest unused index
        index_list[v] = index[0]
        lowlink[v] = index[0]
        onStack[v] = True
        index[0] += 1
        S.append(v)
        
        try:
            for w in graph[v]:
                if index_list.get(w) == None:
                #successor w has not visited yet, recurse on it
                    r = strongconnect(w)
                    if r == -1:
                        return -1
                    lowlink[v] = min(lowlink[v], lowlink[w])
                elif onStack.get(w) != None:
                    # successor w is in stack and hence in the current SCC
                    #w.index not w.lowlink
                    lowlink[v] = min(lowlink[v], index_list[w])
        except:
            pass
        
        #if v is a root node, pop the stack and generate an SCC
        if lowlink[v] == index_list[v]:
            idx = len(SCC)
            #start a new SCC
            SCC.append([])
            while True:
                w = S.pop()
                del onStack[w]
                SCC[idx].append(w)
                inSCC[w] = idx 
                ##if (w > n and (w-n) in SCC[idx]) or (w<n  and (w+n) in SCC[idx]):
                if inSCC.get(-w) != None:
                    if inSCC[w] == inSCC[-w]:
                        return -1
                if result_list.get(w) == None:
                    result_list[w] = True
                    result_list[-w] = False
                    if w > 0:
                        if w % 10 == 1:
                            result[w//10-1] = 'R'
                        elif w % 10 == 2:
                            result[w//10-1] = 'G'
                        elif w % 10 == 3:
                            result[w//10-1] = 'B'
                if w == v:
                    break 
        return
               
    for v in graph.keys():
        if index_list.get(v) == None:
            r = strongconnect(v)
            if r == -1:
                return -1
    #print SCC
    #print result_list
    return result
    

def assign_new_colors(n, edges, colors):
    #global digits_vertices, digits_colors
    # Insert your code here.
    graph = []
    clauses = []
    for i in range(6*n):
        graph.append([])
    # 0-n red true, n-2n green true, 2n-3n blue true; 3n-4n red false; 4n-5n green false; 5n-6n blue false
    # each node one of color:
    clauses = define_clauses(n, edges, colors)   
    #print clauses
    # implication graph
    graph = implication_graph(clauses)
    #print graph
    result = isSatisfiable(graph, n)
    if result == -1:
        return None
    

    return result


def main():
    global digits_vertices, digits_colors
    n, m = map(int, raw_input().split())
    color = raw_input()

    '''
    n, m = 4, 5
    color = 'RRRG'
    '''
    colors = []
    for i in range(len(color)):
        colors.append(color[i])
        
    edges = []


    for i in range(m):
        u, v = map(int, raw_input().split())
        edges.append((u, v))
    '''    

    for i in range(m):
        u, v = map(int, (input_.split()[2*i-2], input_.split()[2*i-1]))
        edges.append((u, v))
    '''
    digits_vertices = range(1, n+1)
    digits_colors = range(1, 4)

    new_colors = assign_new_colors(n, edges, colors)
    if new_colors is None:
        print("Impossible")
    else:
        print(''.join(new_colors))

#main()
# This is to avoid stack overflow issues
threading.Thread(target=main).start()

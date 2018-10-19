# python2 old version

import sys
import threading

# This code is used to avoid stack overflow issues
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**28)  # new thread will get stack of such size

# This solution tries all possible 2^n variable assignments.
# It is too slow to pass the problem.
# Implement a more efficient algorithm here.
def isSatisfiable(graph, n):
    '''
    for mask in range(1<<n):
        result = [ (mask >> i) & 1 for i in range(n) ]
        formulaIsSatisfied = True
        for clause in clauses:
            clauseIsSatisfied = False
            if result[abs(clause[0]) - 1] == (clause[0] < 0):
                clauseIsSatisfied = True
            if result[abs(clause[1]) - 1] == (clause[1] < 0):
                clauseIsSatisfied = True
            if not clauseIsSatisfied:
                formulaIsSatisfied = False
                break
        if formulaIsSatisfied:
            return result
    return None
    
    # constructing an implication graph
    
    graph = {}
    for [i, j] in clauses:
        if graph.get(-i) == None:
            graph[-i] = [j]
        elif j not in graph[-i]:
            graph[-i].append(j)

        if graph.get(-j) == None:
            graph[-j] = [i]
        elif i not in graph[-j]:
            graph[-j].append(i)
    graph = []
    for i in range(2*n):
        graph.append([])
    for [i, j] in clauses:
        if i < 0 and j< 0:
            i = -i
            j = -j
            graph[i-1].append(j-1+n)
            graph[j-1].append(i-1+n)
        elif i < 0 and j >0:
            i = -i
            graph[i-1].append(j-1)
            graph[j-1+n].append(i-1+n)
        elif i > 0 and j < 0:
            j = -j
            graph[i-1+n].append(j-1+n)
            graph[j-1].append(i-1)
        else:
            graph[i-1+n].append(j-1)
            graph[j-1+n].append(i-1)
    '''
    
    SCC = []
    #tarjan algorithm to find SCCs
    index = [0]
    S = []
    inSCC = [None]*(2*n)
    index_list = [None]*(2*n)
    lowlink = [None]*(2*n)
    onStack = [False]*(2*n)  
    '''
    index_list = {}
    lowlink = {}
    onStack = {}
    '''
    #order = toposort(graph)
    #print order
    result_list = [None]*(2*n)
    #result_list = {}
    
        
    def strongconnect(v):
        # set the depth index for v to the smallest unused index
        index_list[v] = index[0]
        lowlink[v] = index[0]
        onStack[v] = True
        index[0] += 1
        S.append(v)
            
        
        for w in graph[v]:
            if index_list[w] == None:
                #successor w has not visited yet, recurse on it
                r = strongconnect(w)
                if r == -1:
                    return -1
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif onStack[w]:
                # successor w is in stack and hence in the current SCC
                #w.index not w.lowlink
                lowlink[v] = min(lowlink[v], index_list[w])

        
        #if v is a root node, pop the stack and generate an SCC
        if lowlink[v] == index_list[v]:
            idx = len(SCC)
            #start a new SCC
            SCC.append([])
            while True:
                w = S.pop()
                onStack[w] = False
                SCC[idx].append(w)
                inSCC[w] = idx 
                ##if (w > n and (w-n) in SCC[idx]) or (w<n  and (w+n) in SCC[idx]):
                if (w >= n and inSCC[w-n] == idx) or (w < n and inSCC[w+n] == idx):
                    return -1
                if result_list[w] == None:
                    if w < n:
                        result_list[w] = w+1
                        result_list[w+n] = 0
                    else:
                        result_list[w] = 0
                        result_list[w-n] = -(w-n+1)
                if w == v:
                    break 
        return
               
    for v in range(len(graph)):
        if index_list[v] == None:
            r = strongconnect(v)
            if r == -1:
                return -1
    #print SCC

    return result_list
    
    
def main():
    n, m = map(int, raw_input().split())
    graph = []
    for i in range(2*n):
        graph.append([])
    for i in range(m):
        (i, j) = list(map(int, raw_input().split()))
        '''
        if graph.get(-i) == None:
            graph[-i] = [j]
        else:
            graph[-i].append(j)

        if graph.get(-j) == None:
            graph[-j] = [i]
        else:
            graph[-j].append(i)
        '''
        if i < 0 and j< 0:
            i = -i
            j = -j
            graph[i-1].append(j-1+n)
            graph[j-1].append(i-1+n)
        elif i < 0 and j >0:
            i = -i
            graph[i-1].append(j-1)
            graph[j-1+n].append(i-1+n)
        elif i > 0 and j < 0:
            j = -j
            graph[i-1+n].append(j-1+n)
            graph[j-1].append(i-1)
        else:
            graph[i-1+n].append(j-1)
            graph[j-1+n].append(i-1)
            
    #clauses = [ list(map(int, raw_input().split())) for i in range(m) ]


    result = isSatisfiable(graph, n)

    if result is -1:
        print("UNSATISFIABLE")
    else:
        print("SATISFIABLE")
        for i in range(n):
            if result[i] == None:
                print i,
            else:
                print result[i],
  
# This is to avoid stack overflow issues
threading.Thread(target=main).start()
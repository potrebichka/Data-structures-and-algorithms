# python2
import itertools
INF = 10 ** 10

import sys
import threading

# This code is used to avoid stack overflow issues
threading.stack_size(2**30)  # new thread will get stack of such size

def read_data():
    n, m = map(int, raw_input().split())
    graph = [[INF] * n for _ in range(n)]
    for _ in range(m):
        u, v, weight = map(int, raw_input().split())
        u -= 1
        v -= 1
        graph[u][v] = graph[v][u] = weight
    return graph

def print_answer((path_weight, path)):
    if path_weight > 10**9:
        path_weight = -1
    print(path_weight)
    for i in range(len(path)):
         path[i] += 1
    if path_weight == -1:
        return
    print(' '.join(map(str, path)))

def optimal_path(graph):

    n = len(graph)
    #C[((1), 1)] = 0
    
    C = {(frozenset([0, idx+1]), idx+1): (dist, [0,idx+1]) for idx,dist in enumerate(graph[0][1:])}

    for s in range(2, n):
        C_ = dict()
        for S in [frozenset(combination) |{0} for combination in itertools.combinations(range(1, n), s)]:
            for i in S - {0}:
                C_[(S, i)] = min([(C[(S - {i}, j)][0] + graph[j][i], C[(S -{i}, j)][1] + [i]) for j in S if j!= 0 and j != i])
        C = C_
        
    result = min([(C[d][0] + graph[0][d[1]], C[d][1]) for d in iter(C)])

    return result


def main():
    print_answer(optimal_path(read_data()))
	
# This is to avoid stack overflow issues
threading.Thread(target=main).start()


#uses python2

import sys
import threading

# This code is used to avoid stack overflow issues
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**26)  # new thread will get stack of such size


class Vertex:
    def __init__(self, weight):
        self.weight = weight
        self.children = []


def ReadTree():
    size = int(raw_input())
    tree = [Vertex(w) for w in map(int, raw_input().split())]
    for i in range(1, size):
        a, b = list(map(int, raw_input().split()))
        tree[a - 1].children.append(b - 1)
        tree[b - 1].children.append(a - 1)
    return tree


def dfs(tree, vertex, parent, D):
    '''
    for child in tree[vertex].children:
        if child != parent:
            dfs(tree, child, vertex)
    '''
    # This is a template function for processing a tree using depth-first search.
    # Write your code here.
    # You may need to add more parameters to this function for child processing.
    if D[vertex] == float("inf"):
        if len(tree[vertex].children) == 0:
            D[vertex] = tree[vertex].weight
        elif len(tree[vertex].children) == 1 and tree[vertex].children[0] == parent:
            D[vertex] = tree[vertex].weight
        else:
            m1 = tree[vertex].weight
            for vertex_u in tree[vertex].children:
                if vertex_u != parent:
                    for vertex_w in tree[vertex_u].children:
                        if vertex_w != vertex:
                            m1 = m1 + dfs(tree, vertex_w, vertex_u, D)
            m0 = 0
            for vertex_u in tree[vertex].children:
                if vertex_u != parent:
                    m0 = m0 + dfs(tree, vertex_u, vertex, D)
            D[vertex] = max(m0, m1)
    return D[vertex]    


def MaxWeightIndependentTreeSubset(tree):
    size = len(tree)
    if size == 0:
        return 0
    # initialise D as infinity
    D = []
    for i in range(size):
        D.append(float("inf"))
    D = dfs(tree, 0, -1, D)
    # You must decide what to return.
    return D


def main():
    tree = ReadTree();
    weight = MaxWeightIndependentTreeSubset(tree);
    print(weight)


# This is to avoid stack overflow issues
threading.Thread(target=main).start()

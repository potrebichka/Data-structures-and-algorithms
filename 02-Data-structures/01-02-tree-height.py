##### python2

import threading, Queue
#sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class Node:
    def __init__(self, index, value):
        self.index = index
        self.value = value
        self.children = []
        
    def addChild(self, child):
        self.children.append(child)
    
    def left(self):
        if len(self.children) > 0:
            return self.children[0]

    def right(self):
        if len(self.children) > 1:
            return self.children[1]
        
    def kids(self):
        if len(self.children) > 0:
            return self.children
        else:
            return None
            
class TreeHeight:
        def read(self):
                self.n = int(raw_input())
                parents = raw_input()
                self.parent = list(map(int, parents.split()))
                self.nodes = []
                for i in range(self.n):
                    self.nodes.append(Node(i, self.parent[i]))
                    
                for child_index in range (self.n):
                    parent_index = self.parent[child_index]
                    if parent_index == -1:
                        self.root = child_index
                    else:
                        self.nodes[parent_index].addChild(self.nodes[child_index])
                        

        def compute_height_primitive(self):
                # Replace this code with a faster implementation
                maxHeight = 0
                for vertex in range(self.n):
                        height = 0
                        i = vertex
                        while i != -1:
                                height += 1
                                i = self.parent[i]
                        maxHeight = max(maxHeight, height)
                return maxHeight
        
        def compute_height(self):
            if len(self.nodes) == 0:
                return
            q = Queue.Queue()
            #for i in range(self.n):
            #    q.put(self.nodes[i])
            q.put([self.nodes[self.root], 1])
            maxHeight = 1
            while not q.empty():
                [node, height] = q.get()
                #print node.index, node.value, height
                if height > maxHeight:
                    maxHeight = height
                if node.kids():
                    for child in node.kids():
                        q.put([child, height + 1])
            return maxHeight

tree = TreeHeight()
tree.read()
print(tree.compute_height())
# python2

import threading, sys
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
    def read(self):
        self.n = int(raw_input())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            a, b, c = map(int, raw_input().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c


    def inOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        if len(self.key) == 0:
            return
        self.inOrder_element(0)
        return self.result
    
    def inOrder_element(self, i):
        if i == -1:
            return
        self.inOrder_element(self.left[i])
        self.result.append(self.key[i])
        self.inOrder_element(self.right[i])
        
    def preOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        if len(self.key) == 0:
            return
        self.preOrder_element(0)
        return self.result
    
    def preOrder_element(self, i):
        if i == -1:
            return
        self.result.append(self.key[i])
        self.preOrder_element(self.left[i])
        self.preOrder_element(self.right[i])

    def postOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        if len(self.key) == 0:
            return
        self.postOrder_element(0)
        return self.result
    
    def postOrder_element(self, i):
        if i == -1:
            return
        self.postOrder_element(self.left[i])
        self.postOrder_element(self.right[i])
        self.result.append(self.key[i])

def main():
    threading.Thread().start()
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()

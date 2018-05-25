#python2
import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

# class defining new Node
class Node:
    def __init__(self, node):
        self.key = node[0]
        self.left = node[1]
        self.right = node[2]

def IsBinarySearchTree(tree):
    # Implement correct algorithm here
    key_min = -2** 31
    key_max = 2** 31 -1
    if len(tree) == 0:
        return True
    return IsBinarySearchTree_Node(tree[0], key_min, key_max)
    
def IsBinarySearchTree_Node(number_node, key_min, key_max):
    # empty tree is binary search tree
    if number_node == None:
        return True
    
    if number_node.key < key_min or number_node.key > key_max:
        return False
    # recursively checking left and right children
    if number_node.left == -1 and number_node.right == -1:
        return True
    elif number_node.left == -1 and not number_node.right == -1:
        return (IsBinarySearchTree_Node(tree[number_node.right], number_node.key, key_max))
    elif not number_node.left == -1 and number_node.right == -1:
        return (IsBinarySearchTree_Node(tree[number_node.left], key_min, number_node.key))
    else:
        return (IsBinarySearchTree_Node(tree[number_node.left], key_min, number_node.key) 
            and IsBinarySearchTree_Node(tree[number_node.right], number_node.key, key_max))
    
    

nodes = int(raw_input())
tree = []
for i in range(nodes):
    node = raw_input().split()
    tree.append(Node(map(int, node)))
    
def main():
    if IsBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")

threading.Thread(target=main).start()
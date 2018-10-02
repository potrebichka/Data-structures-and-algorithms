### Uses python2
import sys

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.
def build_trie(patterns):
    tree = dict()
    # write your code here
    #start from only one node: root
    root = 0
    tree[root] = dict()
    node = 1
	#processing all patterns
    for pattern in patterns:
        current_node = root
		#process pattern symbol by symbol
        for i in range(len(pattern)):
            currentSymbol = str(pattern[i])
			# if symbol in pattern already in tree, check further
            if tree[current_node].get(currentSymbol) != None:
                current_node = tree[current_node][currentSymbol]
            else:
			# else add new node to tree
                tree[node] = dict()
                tree[current_node][currentSymbol] = node
                current_node = node
                node += 1
    return tree


n = int(raw_input())
patterns = []
for i in range(n):
    patterns.append(raw_input())
tree = build_trie(patterns)
#print tree
for node in tree:
    #print 'n', node
    for c in tree[node]:
        #print 'c', c
        print("{}->{}:{}".format(node, tree[node][c], c))

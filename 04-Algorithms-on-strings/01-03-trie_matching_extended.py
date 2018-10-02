# python2
import sys

def build_trie(patterns):
    tree = dict()
    # write your code here
    #start from only one node: root
    root = 0
    tree[root] = dict()
    node = 1
    for pattern in patterns:
        current_node = root
        for i in range(len(pattern)):
            currentSymbol = str(pattern[i])
            if tree[current_node].get(currentSymbol) != None:
                current_node = tree[current_node][currentSymbol]
            else:
                tree[node] = dict()
                tree[current_node][currentSymbol] = node
                current_node = node
                node += 1
        tree[current_node]['$'] = []
    return tree


def solve (text, n, patterns):
    result = []
    # write your code here
    trie = build_trie(patterns)
    position = 0
    while text != "":
        if prefix_trie_matching(text, trie) == 'pattern':
            result.append(position)
        text = text[1:]
        position += 1
    return result

def prefix_trie_matching(text, trie):
    letter = 0
    symbol = text[letter] # first letter of text
    v = 0 # root of Trie
    while True:
        if trie[v].get('$') != None: # if the leaf of trie
            return 'pattern'
        elif trie[v].get(symbol) != None: # if there is an edge
            if letter >= len(text):
                return
            v = trie[v][symbol] #next node in trie
            letter += 1
            symbol = text[letter] if len(text) > letter else None# next letter in text
        else:
            return
        

text = raw_input()
n = int (raw_input())
patterns = []
for i in range (n):
    patterns += [raw_input()]

ans = solve (text, n, patterns)

print (' '.join (map (str, ans)) + '\n')

# python2
import sys


sys.setrecursionlimit(5500)

NA = -1
branch_list = dict()
branch_list['$'] = 0
branch_list['A'] = 1
branch_list['C'] = 2
branch_list['G'] = 3
branch_list['T'] = 4

class Node:
    def __init__ (self):
        self.next_ = [NA] * 5
        self.parent = None
        self.value = None
        self.number = None
        # 0 - $, 1 - A, 2 - C, 3 - G, 4 - T

def build_suffix_tree(text):
    """
    Build a suffix tree of the string text and return a list
    with all of the labels of its edges (the corresponding 
    substrings of the text) in any order.
    """
    result = []
    # Implement this function yourself
    tree = Node()
    while text != '':
        node = tree
        current_text = text
        while True:
            currentSymbol = current_text[0]
            last_text = current_text[1:]
            branch = branch_list[currentSymbol]
            if node.next_[branch] == NA:
                new_node = Node()
                new_node.parent = node
                new_node.value = current_text
                node.next_[branch] = new_node
                break
            elif node.next_[branch].value == current_text:
                break
            elif node.next_[branch].value == currentSymbol:
                node = node.next_[branch]
                current_text = current_text[1:]
            else:
                value = node.next_[branch].value
                counter = 0
                for i in range(max(len(value), len(current_text))):
                    if value[:counter+1] == current_text[:counter+1]:
                        counter += 1
                    else:
                        break
                updated_value = value[:counter]
                if updated_value == value:
                    node = node.next_[branch]
                    current_text = current_text[counter:]
                    continue
                new_node1 = Node()
                new_node1.value = updated_value
                new_node2 = node.next_[branch]
                node.next_[branch] = new_node1
                new_value = value[counter:]
                branch = branch_list[new_value[0]]
                new_node2.value = new_value
                new_node1.next_[branch] = new_node2
                current_text = current_text[counter:]
                node = new_node1
        text = text[1:]
    result = read_suffix_trie(tree, result)[1:]
    return result

def read_suffix_trie(tree, result):
    result.append(tree.value)
    for i in range(5):
        if tree.next_[i] != NA:
            read_suffix_trie(tree.next_[i], result)
    return result

text = raw_input()
result = build_suffix_tree(text)
print("\n".join(result))
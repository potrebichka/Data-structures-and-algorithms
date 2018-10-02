# python2
import sys

sys.setrecursionlimit(5500)

NA = -1
branch_list = dict()
branch_list['$'] = 5
branch_list['A'] = 1
branch_list['C'] = 2
branch_list['G'] = 3
branch_list['T'] = 4
branch_list['#'] = 0

class Node:
    def __init__ (self):
        self.next_ = [NA] * 6
        self.parent = None
        self.value = None
        self.marked = None
        self.marked2 = None
        # 0 - $, 1 - A, 2 - C, 3 - G, 4 - T

def build_suffix_tree(text, length):
    """
    Build a suffix tree of the string text and return a list
    with all of the labels of its edges (the corresponding 
    substrings of the text) in any order.
    """
    result = []
    # Implement this function yourself
    tree = Node()
    position = 0
    while text != '':
        node = tree
        current_text = text
        current_position = position
        while True:
            currentSymbol = current_text[0]
            last_text = current_text[1:]
            branch = branch_list[currentSymbol]
            if node.next_[branch] == NA:
                new_node = Node()
                new_node.parent = node
                new_node.value = current_text
                if (current_position + len(current_text) > length) and current_position <= length:
                    new_node.marked = True
                    new_node.marked2 = True
                else:
                    new_node.marked = False
                    new_node.marked2 = False
                node.next_[branch] = new_node                    
                break
            elif node.next_[branch].value == current_text:
                break
            elif node.next_[branch].value == currentSymbol:
                node = node.next_[branch]
                current_text = current_text[1:]
                current_position += 1
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
                new_node1.parent = node
                if (current_position + len(updated_value) > length) and current_position <= length:
                    new_node1.marked = True
                    new_node1.marked2 = True
                new_node2 = node.next_[branch]
                node.next_[branch] = new_node1
                new_value = value[counter:]
                branch = branch_list[new_value[0]]
                new_node2.value = new_value
                new_node1.next_[branch] = new_node2
                new_node2.parent = new_node1
                current_text = current_text[counter:]
                node = new_node1
        text = text[1:]
        position += 1
    result2 = ''
    check_tree(tree)
    result2 = read_suffix_trie(tree, result2, "")
    return result2

def check_tree(tree):
    if tree.marked == True:
        return True
    elif tree.marked == False:
        return False
    elif tree.marked == None:
        check_branches = []
        for i in range(6):
            if tree.next_[i] != NA:
                check_branch = check_tree(tree.next_[i])
                check_branches.append(check_branch)
        all_var = True
        for var in check_branches:
            all_var = all_var & var
        if all_var:
            tree.marked = True
            return True
        else:
            tree.marked = False
            return False

def read_suffix_trie(tree, result2, parent_value):
    
    for i in range(6):
        if tree.next_[i] != NA:
            par_var = parent_value
            if tree.next_[i].value == None:
                par_var = parent_value
            else:
                par_var = parent_value + tree.next_[i].value
            if tree.next_[i].marked2 == False:
                continue
            elif tree.next_[i].marked2 == True:
                if tree.next_[i].value[0] == '#' and tree.marked == True:
                    result_var = parent_value
                    if len(result2) == 0 or len(result_var) < len(result2):
                        result2 = result_var
                        
                elif tree.next_[i].value[0] == '#' and tree.marked == False:
                    continue
                elif tree.marked == False:
                    result_var = parent_value + tree.next_[i].value[0]
                    if len(result2) == 0 or len(result_var) < len(result2):
                        result2 = result_var
                elif tree.marked == True:
                    result_var = parent_value
                    if len(result2) == 0 or len(result_var) < len(result2):
                        result2 = result_var
            result2 = read_suffix_trie(tree.next_[i], result2, par_var) 
    return result2

def solve (p, q):
    result = p
    text = p + '#' + q + '$'
    res = build_suffix_tree(text, len(p))
    #print("\n".join(res))
    print res
    return result



p = raw_input()
q = raw_input()


ans = solve (p, q)

#sys.stdout.write (ans + '\n')
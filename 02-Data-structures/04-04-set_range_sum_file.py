##### python3

from sys import stdin

# Splay tree implementation

# Vertex of a splay tree
class Vertex:
    def __init__(self, key, summ, left, right, parent):
        (self.key, self.summ, self.left, self.right, self.parent) = (key, summ, left, right, parent)

def update(v):
    if v == None:
        return
    v.summ = v.key + (v.left.summ if v.left != None else 0) + (v.right.summ if v.right != None else 0)
    if v.left != None:
        v.left.parent = v
    if v.right != None:
        v.right.parent = v

def smallRotation(v):
    parent = v.parent
    if parent == None:
        return
    grandparent = v.parent.parent
    if parent.left == v:
        m = v.right
        v.right = parent
        parent.left = m
    else:
        m = v.left
        v.left = parent
        parent.right = m
    update(parent)
    update(v)
    v.parent = grandparent
    if grandparent != None:
        if grandparent.left == parent:
            grandparent.left = v
        else: 
            grandparent.right = v

def bigRotation(v):
    if v.parent.left == v and v.parent.parent.left == v.parent:
        # Zig-zig
        smallRotation(v.parent)
        smallRotation(v)
    elif v.parent.right == v and v.parent.parent.right == v.parent:
        # Zig-zig
        smallRotation(v.parent)
        smallRotation(v)    
    else: 
        # Zig-zag
        smallRotation(v)
        smallRotation(v)

# Makes splay of the given vertex and makes
# it the new root.
def splay(v):
    if v == None:
        return None
    while v.parent != None:
        if v.parent.parent == None:
            smallRotation(v)
            break
        bigRotation(v)
    return v

# Searches for the given key in the tree with the given root
# and calls splay for the deepest visited node after that.
# Returns pair of the result and the new root.
# If found, result is a pointer to the node with the given key.
# Otherwise, result is a pointer to the node with the smallest
# bigger key (next value in the order).
# If the key is bigger than all keys in the tree,
# then result is None.
def find(root_f, key): 
    global root
    v = root_f
    last = root_f
    next_ = None
    while v != None:
        if v.key >= key and (next_ == None or v.key < next_.key):
            next_ = v    
        last = v
        if v.key == key:
            break    
        if v.key < key:
            v = v.right
        else: 
            v = v.left      
    root = splay(last)
    return (next_, root_f)

def split(root, key): 
    (result, root) = find(root, key)
    if result == None:    
        return (root, None)  
    right = splay(result)
    left = right.left
    right.left = None
    if left != None:
        left.parent = None
    update(left)
    update(right)
    return (left, right)

  
def merge(left, right):
    if left == None:
        return right
    if right == None:
        return left
    while right.left != None:
        right = right.left
    right = splay(right)
    right.left = left
    update(right)
    return right

  
# Code that uses splay tree to solve the problem
                                    
root = None

def insert(x):
    global root
    (left, right) = split(root, x)
    new_vertex = None
    if right == None or right.key != x:
        new_vertex = Vertex(x, 0, None, None, None)  
    root = merge(merge(left, new_vertex), right)

    
def erase(x): 
    global root
    # Implement erase yourself
    left, right = split(root, x)
    if root == None:
        return
    if root.right == None:
        root = left
        root = splay(root)
    else:
        y = root.right
        root = splay(y)
        left2, right2 = split(root, y)
        root = merge(left, right2)
    

def search(x): 
    global root
    # Implement find yourself
    next_, root = find(root, x)
    if next_ == None:
        return False
    if next_.key == x:
        return True
    else:
        return False

def sum_(fr, to): 
    global root
    (left, middle) = split(root, fr)
    (middle, right) = split(middle, to + 1)
    ans = 0
    # Complete the implementation of sum
    next_, root = find(middle, fr)
    #if next_ == None:
    #    return 0
    #ans += next_.key
    #print '1', ans
    #while True:

    #    if root.right != None:
    #        root1 = root.right.key
    #        print 'r1', root1
    #        next_, root = find(middle, root1)
    #        ans += next_.key
    #    else:
    #        break
    ans = next_.summ if next_ != None else 0
    root = merge(left, merge(middle, right))
    return ans

MODULO = 1000000001
handler = open('pr_ass_4/set_range_sum/tests/20.txt', 'r')
k = 0
             
last_sum_result = 0
for line in handler:
    if k == 0:
        n = int(line)
    else:
        line = line.split()
        if line[0] == '+':
            x = int(line[1])
            insert((x + last_sum_result) % MODULO)
        elif line[0] == '-':
            x = int(line[1])
            erase((x + last_sum_result) % MODULO)
        elif line[0] == '?':
            x = int(line[1])
            print('Found' if search((x + last_sum_result) % MODULO) else 'Not found')
        elif line[0] == 's':
            l = int(line[1])
            r = int(line[2])
            res = sum_((l + last_sum_result) % MODULO, (r + last_sum_result) % MODULO)
            print(res)
            last_sum_result = res % MODULO
    k+= 1
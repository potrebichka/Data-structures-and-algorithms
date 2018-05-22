#python2
n, m = map(int, raw_input().split())
lines = list(map(int, raw_input().split()))
rank = [1] * n
#rank = list(range(0, n))
parent = list(range(0, n))
ans = max(lines)

def getParent(table):
    # find parent and compress path
    if not (table == parent[table]):
        parent[table] = getParent(parent[table])
    return parent[table]
    #while not (table == parent[table]):
    #    table_new = parent[table]
    #    parent[table] = table
    #    table = table_new
    #return parent[table]

def merge(destination, source):
    global ans, lines, rank
    realDestination, realSource = getParent(destination), getParent(source)

    if realDestination == realSource:
        return False

    # merge two components
    # use union by rank heuristic 
    # update ans with the new maximum table size
    
    #check if height of destination tree is larger than source tree. Destination will be the root

    if rank[realDestination] > rank[realSource]:
        parent[realSource] = realDestination
        lines[realDestination] += lines[realSource]
        if lines[realDestination] > ans:
            ans = lines[realDestination]
        lines[realSource] = 0
    else:
        # the opposite
        parent[realDestination] = realSource
        lines[realSource] += lines[realDestination]
        lines[realDestination] = 0
        if lines[realSource] > ans:
            ans = lines[realSource]
        # if trees has the same height. Rank of new tree is increasing by 1
        if rank[realDestination] == rank[realSource]:
            rank[getParent(realSource)] += 1
    return True

for i in range(m):
    destination, source = map(int, raw_input().split())
    merge(destination - 1, source - 1)
    print(ans)

## python3
import sys
from heapq import heappush, heappop

class BiDij:
    def __init__(self, n):
        self.n = n;                             # Number of nodes
        self.inf = float("inf")                      # All distances in the graph are smaller
        self.d = [[self.inf]*n, [self.inf]*n]   # Initialize distances for forward and backward searches
        self.visited = [False]*n                  # visited[v] == True iff v was visited by forward or backward search
        self.workset = []                      # All the nodes visited by forward or backward search
        #self.prev = [[None for _ in range(n)], [None for _ in range(n)]] 

    def clear(self):
        """Reinitialize the data structures for the next query after the previous query."""
        self.d = [[self.inf]*n, [self.inf]*n]   # Initialize distances for forward and backward searches
        self.visited = [False]*n                  # visited[v] == True iff v was visited by forward or backward search
        self.workset = []     

    def visit(self, pq, side, v):
        """Try to relax the distance to node v from direction side by value dist."""
        # Implement this method yourself
        
        # relax all edges from this node      
        for i in range(len(adj[side][v])):
            u = adj[side][v][i]
            
            if self.d[side][u] > self.d[side][v] + cost[side][v][i]:
                self.d[side][u] = self.d[side][v] + cost[side][v][i]
                # put new node in queue
                heappush(pq[side], (self.d[side][u], u))
        self.workset.append(v)
        #self.visited[v] = True

    def query(self, adj, cost, s, t):
        '''
        if n == 0 or m == 0:
            return -1
        if n == 1:
            return 0'''
        if s == t:
            return 0
        # clear data before new query
        self.clear()
        # new double queue
        pq = [[], []]
        # put edges from s and t in queue
        #initialising distances from s and t node equal zero
        self.d[0][s] = 0
        self.d[1][t] = 0
        self.workset.append(s)
        self.workset.append(t)
        # relax edges from s  and t node
        self.visit(pq, 0, s)
        self.visit(pq, 1, t)
        # case when s and t nodes are the same
        if s == t:
            return self.d[0][t]
        
        # there is no way between nodes
        if not pq[0] and not pq[1]:
            return -1
        
        while pq[0] and pq[1]:
            try:
                # find node with minimum edge
                dist_min, min_vertex = heappop(pq[0])
                # relax that node and if it was in backward search - find shortest way
                self.visit(pq, 0, min_vertex)
                if self.visited[min_vertex]:
                    return self.ShortestPath(min_vertex)
                self.visited[min_vertex] = True
            except:
                continue
            try:
                # for backward search the same
                dist_min, min_vertex = heappop(pq[1])
                self.visit(pq, 1, min_vertex)
                if self.visited[min_vertex]:
                    return self.ShortestPath(min_vertex)
                self.visited[min_vertex] = True
            except:
                continue
        return -1 if self.d[0][t] == float("inf") else self.d[0][t]

    
    def ShortestPath(self, v):
        distance = self.inf
        for u in self.workset:
            if self.d[0][u] +  self.d[1][u] < distance:
                distance =  self.d[0][u] + self.d[1][u]
        return (distance if distance != self.inf else -1)

def readl():
    return map(int, sys.stdin.readline().split())


if __name__ == '__main__':
    n,m = readl()
    adj = [[[] for _ in range(n)], [[] for _ in range(n)]]
    cost = [[[] for _ in range(n)], [[] for _ in range(n)]]
    for e in range(m):
        u,v,c = readl()
        adj[0][u-1].append(v-1)
        cost[0][u-1].append(c)
        adj[1][v-1].append(u-1)
        cost[1][v-1].append(c)
    t, = readl()
    bidij = BiDij(n)
    for i in range(t):
        s, t = readl()
        print(bidij.query(adj, cost, s-1, t-1))

### python2
class MaxMatching:
    def __init__(self):
        self.adj_matrix = []
        self.dist = []
        self.matching = []
    
    def read_data(self):
        
        n, m = map(int, raw_input().split())
        adj_matrix = [list(map(int, raw_input().split())) for i in range(n)]
        """
        n, m = 100, 100
        adj_matrix = [list(map(int, input_.split()[i:100+i])) for i in range(n)]
        """
        return adj_matrix

    def write_response(self, matching):
        line = [str(-1 if x == -1 else x - len(self.adj_matrix)) for x in matching[1:len(self.adj_matrix)+1]]
        print(' '.join(line))

    def find_matching(self):
        # Replace this code with an algorithm that finds the maximum
        # matching correctly in all cases.
        result = 0
        # number of crews - U
        n = len(self.adj_matrix)
        # number of flights - V
        m = len(self.adj_matrix[0])
        
        # stores pair of u in matching
        self.matching = [-1] * (n+m+1)
        self.dist = [float("inf")] * (n+1)
        # while there is an augmenting path, updating
        j = 0
        while self.bfs():
            # find a free vertex
            for u in range(1, n+1):
                # if vertex is free and there is an augmenting path from current vertex
                if self.matching[u] == -1 and self.dfs(u):
                    result += 1
            j += 1
            if j == 10:
                break
        return self.matching
    
    def bfs(self):
        queue = list()

        for u in range(1, len(self.adj_matrix)+1):
            if self.matching[u] == -1:
                self.dist[u] = 0
                queue.append(u)
            else:
                self.dist[u] = float("inf")
        self.dist[0] = float("inf")
        
        while queue:
            u = queue.pop(0)
            if self.dist[u] < self.dist[0]:
                for i in range(len(self.adj_matrix[u-1])):
                    if self.adj_matrix[u-1][i] == 1:
                        vertex_v = i + 1 + len(self.adj_matrix)
                        pair = self.matching[vertex_v]
                        if pair == -1:
                            pair = 0
                        if self.dist[pair] == float("inf"):
                            self.dist[pair] = self.dist[u] + 1
                            queue.append(pair)
        return self.dist[0] != float("inf")
    
    def dfs(self, u):
        if u != 0:
            for i in range(len(self.adj_matrix[u-1])):
                if self.adj_matrix[u-1][i] == 1:
                    v = i + 1 + len(self.adj_matrix)
                    pair = self.matching[v]
                    if pair == -1:
                        pair = 0
                    if self.dist[pair] == self.dist[u] + 1:
                        if self.dfs(pair):
                            self.matching[v] = u
                            self.matching[u] = v
                            return True
            self.dist[u] = float("inf")
            return False
        return True
    
    def solve(self):
        self.adj_matrix = self.read_data()
        matching = self.find_matching()
        self.write_response(matching)

if __name__ == '__main__':
    max_matching = MaxMatching()
    max_matching.solve()
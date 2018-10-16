##### python2
class StockCharts:
    def __init__(self):
        self.adj_matrix = []
        self.dist = []
        self.matching = []
    
    def read_data(self):
        n, k = map(int, raw_input().split())
        stock_data = [list(map(int, raw_input().split())) for i in range(n)]
        return stock_data

    def write_response(self, result):
        print(result)

    def min_charts(self, stock_data):
        # Replace this incorrect greedy algorithm with an
        # algorithm that correctly finds the minimum number
        # of charts on which we can put all the stock data
        # without intersections of graphs on one chart.
        n = len(stock_data)
        k = len(stock_data[0])
        adj = [[] for _ in range(n)]
        
        """
        for new_stock in stock_data:
            added = False
            for chart in charts:
                fits = True
                for stock in chart:
                    above = all([x > y for x, y in zip(new_stock, stock)])
                    below = all([x < y for x, y in zip(new_stock, stock)])
                    if (not above) and (not below):
                        fits = False
                        break
                if fits:
                    added = True
                    chart.append(new_stock)
                    break
            if not added:
                charts.append([new_stock])
        """
        for i in range(len(stock_data)):
            for j in range(len(stock_data)):
                if i != j:
                    stock1 = stock_data[i]
                    stock2 = stock_data[j]
                    above = all([x > y for x, y in zip(stock1, stock2)])
                    if above:
                        adj[i].append(j)
        
        # adj-matrix - bipartite
        self.adj_matrix = [[] for _ in range(n)]
        for i in range(n):
            for j in adj[i]:
                self.adj_matrix[i].append(j + n)      

        result = 0
        # number of crews - U
        n = len(self.adj_matrix)
        # number of flights - V
        
        # stores pair of u in matching
        self.matching = [-1] * (2*n+1)
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
        return n - result
    
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
                for v in self.adj_matrix[u-1]:
                        vertex_v = v + 1
                        pair = self.matching[vertex_v]
                        if pair == -1:
                            pair = 0
                        if self.dist[pair] == float("inf"):
                            self.dist[pair] = self.dist[u] + 1
                            queue.append(pair)
        return self.dist[0] != float("inf")
    
    def dfs(self, u):
        if u != 0:
            for vertex_v in self.adj_matrix[u-1]:
                    v = vertex_v + 1
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
        stock_data = self.read_data()
        result = self.min_charts(stock_data)
        self.write_response(result)

if __name__ == '__main__':
    stock_charts = StockCharts()
    stock_charts.solve()
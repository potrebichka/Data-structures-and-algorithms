# python2

class Edge:

    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = 0

# This class implements a bit unusual scheme for storing edges of the graph,
# in order to retrieve the backward edge for a given edge quickly.
class FlowGraph:

    def __init__(self, n):
        # List of all - forward and backward - edges
        self.edges = []
        # These adjacency lists store only indices of edges in the edges list
        self.graph = [[] for _ in range(n)]

    def add_edge(self, from_, to, capacity):
        # Note that we first append a forward edge and then a backward edge,
        # so all forward edges are stored at even indices (starting from 0),
        # whereas backward edges are stored at odd indices.
        forward_edge = Edge(from_, to, capacity)
        backward_edge = Edge(to, from_, 0)
        self.graph[from_].append(len(self.edges))
        self.edges.append(forward_edge)
        self.graph[to].append(len(self.edges))
        self.edges.append(backward_edge)

    def size(self):
        return len(self.graph)

    def get_ids(self, from_):
        return self.graph[from_]

    def get_edge(self, id):
        return self.edges[id]

    def add_flow(self, id, flow):
        # To get a backward edge for a true forward edge (i.e id is even), we should get id + 1
        # due to the described above scheme. On the other hand, when we have to get a "backward"
        # edge for a backward edge (i.e. get a forward edge for backward - id is odd), id - 1
        # should be taken.
        #
        # It turns out that id ^ 1 works for both cases. Think this through!
        self.edges[id].flow += flow
        self.edges[id ^ 1].flow -= flow


def read_data():
    
    vertex_count, edge_count = map(int, raw_input().split())
    graph = FlowGraph(vertex_count)
    for _ in range(edge_count):
        u, v, capacity = map(int, raw_input().split())
        graph.add_edge(u - 1, v - 1, capacity)
    return graph
    '''
    vertex_count, edge_count = 5, 7
    graph = FlowGraph(vertex_count)
    for i in range(edge_count):
        u, v, capacity = map(int, (input_.split()[3*i], input_.split()[3*i+1], input_.split()[3*i+2]))
        graph.add_edge(u - 1, v - 1, capacity)
   
    return graph'''

def max_flow(graph, from_, to):
    flow = 0
    # your code goes here
    # number of vertices in graph
    n = graph.size()
    while True:
        path = [-1] * n
        path[from_] = -2
        M = [0] * n
        M[from_] = float("infinity")
        pathflow, path = BFS(graph, from_, to, path, M)
        if pathflow == 0:
            break
        flow = flow + pathflow
        vertex_v = to
        while vertex_v != from_:
            vertex_u = path[vertex_v][0]
            id_edge_u_v = path[vertex_v][1]
            graph.add_flow(id_edge_u_v, pathflow)
            vertex_v = vertex_u
    return flow

def BFS(graph, from_, to, path, M):
    # queue for BFS
    BFS_queue = []
    BFS_queue.append(from_)
    while BFS_queue:
        vertex_u = BFS_queue.pop(0)
        for id_v in graph.get_ids(vertex_u):
            edge_u_v = graph.get_edge(id_v)
            vertex_v = edge_u_v.v
            if (edge_u_v.capacity - edge_u_v.flow) > 0 and path[vertex_v] == -1:
                path[vertex_v] = (vertex_u, id_v)
                M[vertex_v] = min(M[vertex_u], edge_u_v.capacity - edge_u_v.flow)
                if vertex_v != to:
                    BFS_queue.append(vertex_v)
                else:
                    return M[to], path
    return 0, path


if __name__ == '__main__':
    graph = read_data()
    print(max_flow(graph, 0, graph.size() - 1))
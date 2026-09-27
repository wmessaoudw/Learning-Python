#Adjacency Matrix In Python O(1) look up O(V**2) memory

class GraphAdjacencyMatrix:
    def __init__(self, num_vertices):
        self.v = num_vertices

        self.matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, u, v, weight=1, directed=False):

        if 0 <= u < self.v and 0 <= v < self.v:
            self.matrix[u][v] = weight
            if not directed:
                self.matrix[v][u] = weight

    def remove_edge(self, u, v, directed=False):

        if 0 <= u < self.v and 0 <= v < self.v:
            self.matrix[u][v] = 0
            if not directed:
                self.matrix[v][u] = 0

    def has_edge(self, u, v):

        return self.matrix[u][v] != 0

    def print_matrix(self):
        print("Adjacency Matrix:")
        for row in self.matrix:
            print(" ".join(map(str, row)))

#Adjacency List In Python O(V) look up O(V+E) memory
class GraphAdjacencyList:
    def __init__(self):

        self.adj_list = {}

    def add_vertex(self, vertex):

        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, u, v, weight=None, directed=False):

        self.add_vertex(u)
        self.add_vertex(v)


        if weight is None:
            self.adj_list[u].append(v)
            if not directed:
                self.adj_list[v].append(u)

        else:
            self.adj_list[u].append((v, weight))
            if not directed:
                self.adj_list[v].append((u, weight))

    def remove_edge(self, u, v, directed=False):

        if u in self.adj_list and v in self.adj_list[u]:
            self.adj_list[u].remove(v)
        if not directed and v in self.adj_list and u in self.adj_list[v]:
            self.adj_list[v].remove(u)

    def print_graph(self):

        print("Adjacency List:")
        for vertex, neighbors in self.adj_list.items():
            print(f"{vertex} -> {neighbors}")




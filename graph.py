class Graph:
    def __init__(self):
        self.graph = {}

    def has_vertex(self, vertex):
        if vertex in self.graph:
            return True
        else:
            return False

    def has_edge(self, vertex1, vertex2):
        if not self.has_vertex(vertex1) or not self.has_vertex(vertex2):
            return False
        if vertex2 in self.graph[vertex1]:
            return True
        else:
            return False

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = {}

    def remove_vertex(self, vertex):
        if vertex in self.graph:
            del self.graph[vertex]
        for v in self.graph:
            self.remove_edge(v, vertex)

    def add_edge(self, vertex1, vertex2):
        if self.has_vertex(vertex1) and self.has_vertex(vertex2):
            if not self.has_edge(vertex1, vertex2):
                self.graph[vertex1][vertex2] = 1
            else:
                self.graph[vertex1][vertex2] += 1

    def remove_edge(self, vertex1, vertex2):
        if self.has_edge(vertex1, vertex2):
            del self.graph[vertex1][vertex2]

    def weight(self, vertex1, vertex2):
        if not self.has_edge(vertex1, vertex2):
            return 0
        else:
            return self.graph[vertex1][vertex2]

    def get_vertices(self):
        return list(self.graph.keys())

    def get_edges(self, vertex):
        return list(self.graph[vertex].keys())
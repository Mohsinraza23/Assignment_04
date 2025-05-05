# graph.py
import random

class Vertex:
    def __init__(self, word):
        self.word = word
        self.edges = {}
        self.neighbors = []
        self.weights = []

    def add_edge_to(self, vertex, weight=0):
        self.edges[vertex] = weight

    def increment_edge(self, vertex):
        self.edges[vertex] = self.edges.get(vertex, 0) + 1

    def get_edges(self):
        return self.edges.keys()

    def compute_edge_weights(self):
        self.neighbors = []
        self.weights = []
        for vertex, weight in self.edges.items():
            self.neighbors.append(vertex)
            self.weights.append(weight)

    def next_word(self):
        if not self.neighbors:
            return None
        return random.choices(self.neighbors, weights=self.weights)[0]

class Graph:
    def __init__(self):
        self.vertices = {}

    def get_vertex(self, word):
        if word not in self.vertices:
            self.vertices[word] = Vertex(word)
        return self.vertices[word]

    def add_edge(self, from_vertex, to_vertex):
        from_vertex.increment_edge(to_vertex)

    def get_next_word(self, current_vertex):
        return current_vertex.next_word()

    def generate_probability_mapping(self):
        for vertex in self.vertices.values():
            vertex.compute_edge_weights()
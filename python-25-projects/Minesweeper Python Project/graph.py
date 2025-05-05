import random

class Vertex:
    def __init__(self, value):
        self.value = value
        self.adjacent = {}
        self.probabilities = []

    def add_edge(self, vertex):
        if vertex in self.adjacent:
            self.adjacent[vertex] += 1
        else:
            self.adjacent[vertex] = 1

    def generate_probabilities(self):
        total = sum(self.adjacent.values())
        self.probabilities = []
        for vertex, count in self.adjacent.items():
            self.probabilities.extend([vertex.value] * count)

    def next_word(self):
        if not self.probabilities:
            return None
        return random.choice(self.probabilities)

class Graph:
    def __init__(self):
        self.vertices = {}

    def get_vertex(self, value):
        if value not in self.vertices:
            self.vertices[value] = Vertex(value)
        return self.vertices[value]

    def add_edge(self, from_vertex, to_vertex):
        self.vertices[from_vertex.value].add_edge(to_vertex)

    def generate_probability_mapping(self):
        for vertex in self.vertices.values():
            vertex.generate_probabilities()

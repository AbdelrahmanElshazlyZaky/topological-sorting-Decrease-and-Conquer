from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.vertices = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topological_sort_util(self, v, visited, stack):
        visited[v] = True

        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.topological_sort_util(neighbor, visited, stack)

        stack.append(v)

    def topological_sort(self):
        visited = [False] * self.vertices
        stack = []

        for i in range(self.vertices):
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)

        return stack[::-1]


graph = Graph(5)
graph.add_edge(0, 2)
graph.add_edge(1, 0)
graph.add_edge(1, 3)
graph.add_edge(3, 2)
graph.add_edge(4, 1)
graph.add_edge(4, 3)

result = graph.topological_sort()
print("Topological Sorting Order:")
print (result)
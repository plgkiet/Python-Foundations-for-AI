from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    #bfs with undirected graph
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, n):
        visited_vertices = [False]*(len(self.graph))

        queue = []
        visited_vertices[n] = True
        queue.append(n)

        while queue:
            n = queue.pop(0)
            print(n, end=" ")
            for v in self.graph[n]:
                if not visited_vertices[v]:
                    queue.append(v)
                    visited_vertices[v] = True


graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(3, 4)

print ( " The Breadth First Search Traversal for The Graph is as Follows: " ) 
graph.bfs(0)



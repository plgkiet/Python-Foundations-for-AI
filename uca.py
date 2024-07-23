import heapq
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.cost = {}

    def addEdge(self, u, v, w):
        self.graph[u].append(v)
        self.cost[(u, v)] = w
    
def uniform_cost_search(graph_obj, goal, start):
    graph, cost = graph_obj.graph, graph_obj.cost
    answer = []

    for _ in range(len(goal)):
        answer.append(10**8)

    queue = [(0, start)]
    heapq.heapify(queue)
    visited = {}
    count = 0

    while queue:
        p = heapq.heappop(queue)  
        cost_so_far, node = p

        if node in goal:
            index = goal.index(node)
            if answer[index] == 10**8:
                count += 1
            if answer[index] > cost_so_far:
                answer[index] = cost_so_far
            if count == len(goal):
                return answer

        if node not in visited:
            for neighbor in graph[node]:
                heapq.heappush(queue, (cost_so_far + cost[(node, neighbor)], neighbor))
            visited[node] = 1

    return answer

if __name__ == '__main__':
    g = Graph()

    g.addEdge(0, 1, 2)
    g.addEdge(0, 3, 5)
    g.addEdge(1, 6, 1)
    g.addEdge(3, 1, 5)
    g.addEdge(3, 6, 6)
    g.addEdge(3, 4, 2)
    g.addEdge(4, 2, 4)
    g.addEdge(4, 5, 3)
    g.addEdge(2, 1, 4)
    g.addEdge(5, 2, 6)
    g.addEdge(5, 6, 3)
    g.addEdge(6, 4, 7)

    goal = [6]

    answer = uniform_cost_search(g, goal, 0)
    print("Chi phí nhỏ nhất từ 0 đến 6 là =", answer[0])

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)


# Khởi tạo một đồ thị
g = Graph()

# Thêm các cạnh vào đồ thị
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)

# In danh sách kề của đỉnh 1
print(g.graph[3])  # Kết quả: [2, 3]

def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    print(node, end=' ')
    if node in graph:
        for neighbour in graph[node]:
            if neighbour not in visited:
                dfs_recursive(graph, neighbour, visited)
    return visited

def dfs_iterative(graph, start):
    stack = [start]
    visited = set()
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node, end=' ')
            # Đảo ngược danh sách kề và kiểm tra từng đỉnh kề
            if node in graph:  # Kiểm tra node có trong graph hay không
                for neighbour in reversed(graph[node]):
                    if neighbour not in visited:
                        stack.append(neighbour)
    return visited


# Ví dụ sử dụng:
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E'],
    'C': ['G', 'F'],
    'D': ['H'],
    'E': ['I'],
    'F': ['J'],
    'G': ['K']
}

print("DFS Đệ Quy:")
# dfs_recursive(graph, 'A')
dfs_iterative(graph, 'A')

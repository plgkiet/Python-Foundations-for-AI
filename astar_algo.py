import heapq

class Node:
    def __init__(self, x, y, cost=0, parent=None):
        self.x = x
        self.y = y
        self.cost = cost
        self.parent = parent
        self.g = float('inf')  # Cost from start node to this node
        self.h = float('inf')  # Heuristic (estimated cost from this node to goal)
        self.f = float('inf')  # Total estimated cost

    def __lt__(self, other):
        return self.f < other.f

def heuristic(node, goal):
    # Manhattan distance heuristic
    return abs(node.x - goal.x) + abs(node.y - goal.y)

def astar(grid, start, goal):
    rows = len(grid)
    cols = len(grid[0])
    open_list = []
    closed_list = set()
    start_node = Node(start[0], start[1], grid[start[0]][start[1]])
    goal_node = Node(goal[0], goal[1])
    
    start_node.g = 0
    start_node.h = heuristic(start_node, goal_node)
    start_node.f = start_node.g + start_node.h
    
    heapq.heappush(open_list, start_node)
    
    while open_list:
        current_node = heapq.heappop(open_list)
        closed_list.add((current_node.x, current_node.y))
        
        if current_node.x == goal_node.x and current_node.y == goal_node.y:
            path = []
            while current_node:
                path.append((current_node.x, current_node.y))
                current_node = current_node.parent
            return path[::-1]  # Return reversed path
        
        neighbors = [(current_node.x + 1, current_node.y),
                     (current_node.x - 1, current_node.y),
                     (current_node.x, current_node.y + 1),
                     (current_node.x, current_node.y - 1)]
        
        for neighbor in neighbors:
            neighbor_x, neighbor_y = neighbor
            if 0 <= neighbor_x < rows and 0 <= neighbor_y < cols:
                if grid[neighbor_x][neighbor_y] != -1 and (neighbor_x, neighbor_y) not in closed_list:
                    neighbor_node = Node(neighbor_x, neighbor_y, grid[neighbor_x][neighbor_y], current_node)
                    neighbor_node.g = current_node.g + neighbor_node.cost
                    neighbor_node.h = heuristic(neighbor_node, goal_node)
                    neighbor_node.f = neighbor_node.g + neighbor_node.h
                    
                    heapq.heappush(open_list, neighbor_node)
                    closed_list.add((neighbor_x, neighbor_y))
    
    return None  # No path found

# Example usage:
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)
goal = (4, 4)

path = astar(grid, start, goal)
if path:
    print("Path found:", path)
else:
    print("No path found")

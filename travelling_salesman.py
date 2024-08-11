# Number of cities (vertices)
V = 4

# List to store the minimum weight Hamiltonian Cycle
answer = []

# Function to find the minimum weight Hamiltonian Cycle
def tsp(graph, v, currPos, n, count, cost):
    # If last node is reached and it has a link to the starting node (source)
    if count == n and graph[currPos][0]:
        answer.append(cost + graph[currPos][0])
        return

    # Backtracking step: Traverse the adjacency list of currPos node
    for i in range(n):
        if not v[i] and graph[currPos][i]:
            # Mark as visited
            v[i] = True
            tsp(graph, v, i, n, count + 1, cost + graph[currPos][i])
            # Mark ith node as unvisited for backtracking
            v[i] = False

# Driver code
if __name__ == "__main__":
    # Example graph represented as a 2D list
    graph = [[0, 10, 15, 20],
             [10, 0, 35, 25],
             [15, 35, 0, 30],
             [20, 25, 30, 0]]

    # Boolean array to check if a node has been visited
    v = [False] * V

    # Mark the starting city (0th node) as visited
    v[0] = True

    # Find the minimum weight Hamiltonian Cycle
    tsp(graph, v, 0, V, 1, 0)

    # Output the minimum cost of the Hamiltonian Cycle
    print("The minimum cost of the Hamiltonian Cycle is:", min(answer))

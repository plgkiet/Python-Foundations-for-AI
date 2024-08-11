# Python program to solve the 8-Queens problem using Backtracking

# Global variable for board size
N = 8

# Function to print the solution
def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()
    print()

# Function to check if a queen can be placed on board[row][col]
def isSafe(board, row, col):
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

# Recursive utility function to solve the 8-Queens problem
def solveNQUtil(board, col):
    # Base case: If all queens are placed
    if col >= N:
        return True

    # Consider this column and try placing this queen in all rows one by one
    for i in range(N):
        if isSafe(board, i, col):
            # Place this queen on board[i][col]
            board[i][col] = 1

            # Recur to place the rest of the queens
            if solveNQUtil(board, col + 1) == True:
                return True

            # If placing queen in board[i][col] doesn't lead to a solution, then backtrack
            board[i][col] = 0

    return False

# Main function to solve the 8-Queens problem
def solveNQ():
    # Initialize the chessboard with zeros
    board = [[0 for _ in range(N)] for _ in range(N)]

    if solveNQUtil(board, 0) == False:
        print("Solution does not exist")
        return False

    printSolution(board)
    return True

# Driver program to test the above functions
solveNQ()

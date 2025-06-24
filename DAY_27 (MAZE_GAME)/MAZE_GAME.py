def print_maze(maze, path=[]):
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if (row, col) in path:
                print("P", end=" ")  # Mark the path with 'P'
            else:
                print(maze[row][col], end=" ")
        print()

def is_valid_move(maze, row, col, visited):
    # Check if the move is inside the maze bounds and not visited, and it's an open path (0)
    return (0 <= row < len(maze)) and (0 <= col < len(maze[0])) and maze[row][col] == 0 and (row, col) not in visited

def solve_maze(maze):
    start = (0, 0)  # Starting position (top-left corner)
    end = (len(maze) - 1, len(maze[0]) - 1)  # Ending position (bottom-right corner)
    path = []
    visited = set()

    def dfs(position):
        if position == end:
            path.append(position)
            return True
        
        row, col = position
        if not is_valid_move(maze, row, col, visited):
            return False

        visited.add(position)
        path.append(position)

        # Explore neighbors (up, down, left, right)
        if dfs((row - 1, col)):  # Move up
            return True
        if dfs((row + 1, col)):  # Move down
            return True
        if dfs((row, col - 1)):  # Move left
            return True
        if dfs((row, col + 1)):  # Move right
            return True

        path.pop()  # Backtrack if no valid move
        return False

    if dfs(start):
        return path  # Return the path if a solution is found
    else:
        return None  # Return None if no solution is found

if __name__ == "__main__":
    # Example maze (0: open path, 1: wall)
    maze = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]

    print("Maze:")
    print_maze(maze)

    path = solve_maze(maze)

    if path:
        print("\nPath found:")
        print_maze(maze, path)
    else:
        print("\nNo path found.")

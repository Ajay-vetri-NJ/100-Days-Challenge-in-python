def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    return True

def solve_nqueens(board, col):
    if col >= len(board):
        print_board(board)
        return True

    res = False
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 'Q'
            res = solve_nqueens(board, col + 1) or res
            board[i][col] = '.'
    
    return res

def solve(N):
    board = [['.' for _ in range(N)] for _ in range(N)]
    if not solve_nqueens(board, 0):
        print("Solution does not exist")
    return

N = int(input("Enter the value of N: "))
solve(N)
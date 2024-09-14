def print_board(board):
    """Print the chessboard with queens placed."""
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))
    print()

def is_safe(board, row, col):
    """Check if a queen can be placed on board[row][col]."""
    # Check this column on the left side
    for i in range(col):
        if board[row][i]:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j]:
            return False

    return True

def solve_n_queens(board, col):
    """Solve the N-Queens problem using backtracking."""
    if col >= len(board):
        return True

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = True
            if solve_n_queens(board, col + 1):
                return True
            board[i][col] = False

    return False

def main():
    N = 8  # Size of the chessboard
    board = [[False] * N for _ in range(N)]

    if solve_n_queens(board, 0):
        print("Solution found:")
        print_board(board)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()

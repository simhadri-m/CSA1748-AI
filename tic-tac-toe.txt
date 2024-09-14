# Tic-Tac-Toe Game

def print_board(board):
    """Prints the current state of the Tic-Tac-Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    """Checks if the given player has won the game."""
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # Check rows
            return True
        if all([board[j][i] == player for j in range(3)]):  # Check columns
            return True
    if all([board[i][i] == player for i in range(3)]):  # Check main diagonal
        return True
    if all([board[i][2 - i] == player for i in range(3)]):  # Check anti-diagonal
        return True
    return False

def check_draw(board):
    """Checks if the game is a draw (i.e., the board is full with no winner)."""
    return all([cell != " " for row in board for cell in row])

def get_move(board):
    """Prompts the player for a valid move."""
    while True:
        try:
            row = int(input("Enter row (1-3): ")) - 1
            col = int(input("Enter column (1-3): ")) - 1
            if board[row][col] == " ":
                return row, col
            else:
                print("Cell already occupied! Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter numbers between 1 and 3.")

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    while True:
        print(f"\nPlayer {current_player}'s turn.")
        print_board(board)

        # Get player's move
        row, col = get_move(board)
        board[row][col] = current_player

        # Check for a winner
        if check_winner(board, current_player):
            print_board(board)
            print(f"\nPlayer {current_player} wins!")
            break

        # Check for a draw
        if check_draw(board):
            print_board(board)
            print("\nIt's a draw!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

# Run the Tic-Tac-Toe game
if __name__ == "__main__":
    tic_tac_toe()

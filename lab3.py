# Task 1: Display the Board
def display_board(board):
    """
    Displays the current state of the Tic Tac Toe board in a readable format:

         X | O | X
        ---|---|---
           | X | O
        ---|---|---
         O |   | X

    :param board (list): A 3x3 2D list representing the game board.
    :return (None): Prints the current state of the board.
    """
    for r in range(len(board)):
        print(f' {board[r][0]} | {board[r][1]} | {board[r][2]} ')

        if r < 2:
            print('---|---|---')

# Task 2: Validate the Move
def is_valid_move(board, row, col):
    """
    Checks if a move is valid. A move is valid if the position is within bounds
    and the cell is empty (' ').

    :param board (list): A 3x3 2D list representing the game board.
    :param row (int): The row index of the move.
    :param col (int): The column index of the move.
    :return (bool): True if the move is valid, False otherwise.
    """
    if not (0 <= row <= 2):
        return False

    if not (0 <= col <= 2):
        return False

    if board[row][col] != ' ':
        return False

    return True

# Task 3: Make the Move
def make_move(board, row, col, player):
    """
    Updates the board with the player's move.

    :param board (list): A 3x3 2D list representing the game board.
    :param row (int): The row index of the move.
    :param col (int): The column index of the move.
    :param player (str): The player's symbol ('X' or 'O').
    :return (None): Updates the board in place.
    """
    board[row][col] = player

# Task 4: Check for a Winner
def check_winner(board):
    """
    Checks if a player has won the game. A player wins if they have three of
    their symbols in a row, column, or diagonal.

    :param board (list): A 3x3 2D list representing the game board.
    :return (str): 'X' if player X wins, 'O' if player O wins, 'None' otherwise.
    """
    for r in range(len(board)):
        if board[r][0] == board[r][1] == board[r][2] and board[r][0] != ' ':
            return board[r][0]

    for c in range(len(board)):
        if board[0][c] == board[1][c] == board[2][c] and board[1][c] != ' ':
            return board[1][c]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[1][1]

    if board[0][2] == board[1][1] == board[2][0] and board[2][0] != ' ':
        return board[1][1]

    return 'None'

# Task 5: Check for a Tie
def is_tie(board):
    """
    Checks if the game has ended in a tie. A tie occurs if the board is full
    and no player has won.

    :param board (list): A 3x3 2D list representing the game board.
    :return (bool): True if the game is a tie, False otherwise.
    """
    for r in range(3):
        for c in range(3):
            if board[r][c] == ' ':
                return False
    return True


# Task 6: Main Game Loop
def main(board):
    """
    The main game loop for Tic Tac Toe. Manages the game flow, alternates turns
    between two players, and checks for a winner or tie after each move.

    :return (None): Prints the game result and manages the game flow.
    """
    # Define player symbols
    players = ['X', 'O']
    turn = 0

    while True:
        # Display the current board state
        display_board(board)

        # Get current player's move
        player = players[turn % 2]
        print(f"Player {player}'s turn.")

        # Input move
        row, col = map(int, input("Enter your move (row and column, space-separated, 0-2): ").split())

        # Validate the move
        if is_valid_move(board, row, col):
            make_move(board, row, col, player)
        else:
            print("Invalid move. Try again.")
            continue

        # Check for a winner
        winner = check_winner(board)
        if winner != 'None':
            display_board(board)
            print(f"Player {winner} wins!")
            break

        # Check for a tie
        if is_tie(board):
            display_board(board)
            print("It's a tie!")
            break

        # Switch turns
        turn += 1

# Entry Point of the Script
if __name__ == "__main__":
    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]

    main(board)

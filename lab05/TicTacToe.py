# Two-player Tic-Tac-Toe game

# Create a 3x3 game board using a 2D list
board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

# Create a list of players
players = ["X", "O"]

# Track the number of turns
turns = 0

# Store the winner of the game
winner = None

# Main game loop
while turns < 9 and winner is None:

    print("\nTIC-TAC-TOE")

    for row in board:
        for index, cell in enumerate(row):
            print(cell, end="")
            if index < 2:
                print(" | ", end="")
        print()

    # Determine whose turn it is
    current_player = players[turns % 2]

    print(f"\n{current_player}'s Turn")

    try:
        row = int(input("Enter row (1-3): "))
        col = int(input("Enter column (1-3): "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        input("Hit [enter] to continue.")
        continue

    # Check if the row and column are valid
    if row < 1 or row > 3 or col < 1 or col > 3:
        print("Invalid position! Choose numbers 1-3.")
        input("Hit [enter] to continue.")
        continue

    row_index = row - 1
    col_index = col - 1

    # Check whether the selected spot is taken
    if board[row_index][col_index] != "-":
        print(f"Someone has already claimed {row}:{col}!")
        input("Hit [enter] to continue.")
        continue

    # Place the player's marker on the board
    board[row_index][col_index] = current_player

    # Check for horizontal and vertical wins
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == current_player:
            winner = current_player

        if board[0][i] == board[1][i] == board[2][i] == current_player:
            winner = current_player

    # Check for diagonal wins
    if board[0][0] == board[1][1] == board[2][2] == current_player:
        winner = current_player

    if board[0][2] == board[1][1] == board[2][0] == current_player:
        winner = current_player

    # Increment the turn counter
    turns += 1

# Display the final game board
print("\nTIC-TAC-TOE")

for row in board:
    for index, cell in enumerate(row):
        print(cell, end="")
        if index < 2:
            print(" | ", end="")
    print()

# Announce the winner or a draw
if winner is not None:
    print(f"\n{winner} won!")
else:
    print("\nIt's a draw!")

print("Game Over! Thanks for playing!")

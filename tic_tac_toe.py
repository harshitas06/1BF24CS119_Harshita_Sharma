
# Tic Tac Toe Game

board = [" " for i in range(9)]

# Display the board
def display_board():
    print()
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("---------")
    print()

# Check winner
def check_winner(player):
    win_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in win_positions:
        if board[a] == board[b] == board[c] == player:
            return True

    return False

# Main game
def play_game():
    current_player = "X"

    for turn in range(9):
        display_board()

        print("Player", current_player)
        position = int(input("Enter position (1-9): ")) - 1

        # Check valid position
        if position < 0 or position > 8 or board[position] != " ":
            print("Invalid position! Try again.")
            continue

        board[position] = current_player

        # Check winner
        if check_winner(current_player):
            display_board()
            print("Player", current_player, "wins!")
            return

        # Switch player
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

    display_board()
    print("Game Draw!")

play_game()

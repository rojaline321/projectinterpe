def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows
    if any(all(cell == player for cell in row) for row in board):
        return True

    # Check columns
    if any(all(board[row][col] == player for row in range(3)) for col in range(3)):
        return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["P1", "P2"]
    turn = 0

    print("Welcome to Tic Tac Toe!")

    while not check_winner(board, "P1") and not check_winner(board, "P2") and not is_board_full(board):
        print_board(board)
        move = int(input(f"{players[turn]}, enter your move (1-9): "))
        row, col = (move - 1) // 3, (move - 1) % 3

        if board[row][col] == " ":
            board[row][col] = players[turn]
            turn = 1 - turn
        else:
            print("Cell is already occupied. Try again.")

    print_board(board)

    if check_winner(board, "P1"):
        print("Player P1 wins!")
    elif check_winner(board, "P2"):
        print("Player P2 wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    play_tic_tac_toe()
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    player_idx = 0

    while True:
        current_player = players[player_idx]
        print_board(board)

        while True:
            try:
                row = int(input(f"Player {current_player}, enter row (0-2): "))
                col = int(input(f"Player {current_player}, enter column (0-2): "))
                if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Congratulations! Player {current_player} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        player_idx = (player_idx + 1) % 2

if __name__ == "__main__":
    play_tic_tac_toe()

#!/usr/bin/python3
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    return None

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    turns = 0
    while turns < 9 and not check_winner(board):
        print_board(board)
        try:
            row_input = input("Enter row (0, 1, or 2) for player " + player + " or 'exit' to quit: ")
            if row_input.lower() == 'exit':
                print("Game exited by user.")
                return
            row = int(row_input)
            col_input = input("Enter column (0, 1, or 2) for player " + player + " or 'exit' to quit: ")
            if col_input.lower() == 'exit':
                print("Game exited by user.")
                return
            col = int(col_input)
            if 0 <= row <= 2 and 0 <= col <= 2:
                if board[row][col] == " ":
                    board[row][col] = player
                    turns += 1
                    if check_winner(board):
                        break
                    player = "O" if player == "X" else "X"
                else:
                    print("That spot is already taken! Try again.")
            else:
                print("Row and column numbers must be between 0 and 2.")
        except ValueError:
            print("Please enter valid integers for row and column.")
        except EOFError:
            print("Game exited by user using EOF.")
            return

    print_board(board)
    if check_winner(board):
        print("Player " + check_winner(board) + " wins!")
    else:
        print("It's a draw!")

tic_tac_toe()


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def get_available_moves(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]

def minimax(board, is_maximizing):
    if check_win(board, "O"):
        return 1
    elif check_win(board, "X"):
        return -1
    elif is_full(board):
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for r, c in get_available_moves(board):
            board[r][c] = "O"
            score = minimax(board, False)
            board[r][c] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for r, c in get_available_moves(board):
            board[r][c] = "X"
            score = minimax(board, True)
            board[r][c] = " "
            best_score = min(score, best_score)
        return best_score

def computer_move(board):
    best_score = -float("inf")
    best_move = None
    for r, c in get_available_moves(board):
        board[r][c] = "O"
        score = minimax(board, False)
        board[r][c] = " "
        if score > best_score:
            best_score = score
            best_move = (r, c)
    return best_move

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]

    while True:
        print_board(board)
        print("Your turn (X):")
        
        try:
            row = int(input("Enter row (0, 1, 2): "))
            col = int(input("Enter column (0, 1, 2): "))
        except ValueError:
            print("Invalid input. Use numbers 0 to 2.")
            continue

        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
            board[row][col] = "X"
        else:
            print("Invalid move. Try again.")
            continue

        if check_win(board, "X"):
            print_board(board)
            print("Congratulations! You win!")
            break
        elif is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Computer's move
        print("Computer's turn (O):")
        r, c = computer_move(board)
        board[r][c] = "O"

        if check_win(board, "O"):
            print_board(board)
            print("Computer wins! Better luck next time.")
            break
        elif is_full(board):
            print_board(board)
            print("It's a draw!")
            break

# Run the game
tic_tac_toe()

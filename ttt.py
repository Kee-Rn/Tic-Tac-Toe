def print_board(board):
    print("-----------")
    for i in range(3):
        print("|", board[i][0], "|", board[i][1], "|", board[i][2], "|")
        print("-----------")
def get_move(player):
    while True:
        move = input(f"{player}, enter your move (row,col): ")
        try:
            row, col= map(int, move.split(","))
            if row < 0 or row > 2 or col < 0 or col >2:
                print("Invalid input. Try again")
            else:
                return (row, col)
        except ValueError:
            print("Invalid Input")

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][1] !="-":
            return board[i][1]
        if board[0][i] == board[1][i] == board[2][1] and board[0][i] !="-":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "-":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "-":
        return board[0][2]
    return None
def play_game():
    board = [["-", "-", "-"],["-", "-", "-"],["-", "-", "-"]]
    player = "X"

    while True:
        print_board(board)
        row, col = get_move(player)
        if board[row][col] != "-":
            print("Cell already occupied.")
            continue
        board[row][col] = player
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"{winner} wins")
            break
        if all([cell != "-" for row in board for cell in row]):
            print_board(board)
            print("It's a tie!")
            break
        player = "O" if player == "X" else "X"
play_game()

board = list (range(1, 10))


def board_creation(board):
    print(" ___________")
    for i in range(3):
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print(" ___________")


def insert_xo(player_xo):
    busy_cell = False
    while not busy_cell:
        player_move = input("Выберите номер клетки для" + player_xo)
        if player_move is not int(player_move):
            print("Ошибка ввода, вы должны ввести число от 1 до 9")
        else:
            continue
        player_move=int(player_move)
        if player_move >= 1 and player_move <= 9:
            if str(board[player_move-1]) not in "XO":
                board[player_move-1] = player_xo
            busy_cell = True
        else:
            print("Эта клетка уже занята, выберите другую")
    else:
        print("Вам необходимо ввести номер клетки от 1 до 9")


def win_condition(board):
    win_cells = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for check in win_cells:
        if board[check[0]] == board[check[1]] == board[check[2]]:
            return board[check[0]]
        return False


def summarizing(board):
    counter = 0
    winner = False
    while not winner:
        board_creation(board)
        if counter % 2 == 0:
            player_xo = "X"
        else:
            player_xo = "O"
        insert_xo(player_xo)
        counter += 1
        if counter > 4:
            win_condition(board)
            if win_condition(board):
                print("Ты победил!")
                winner = True
                break
        if counter == 9:
            print("Ничья!")
            break


summarizing(board)
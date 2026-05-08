
size = int(input("Enter board size: "))

board = []
for i in range(size):
    row = []
    for j in range(size):
        row.append("-")
    board.append(row)

player = "X"
moves = 0

while moves < size * size:

    for r in board:
        print(" ".join(r))

    print("Player", player)
    row = int(input("Enter row: "))
    col = int(input("Enter column: "))

    if board[row][col] == "-":
        board[row][col] = player
        moves += 1
    else:
        print("Place already filled")
        continue

    win = False

    # check rows
    for i in range(size):
        count = 0
        for j in range(size):
            if board[i][j] == player:
                count += 1
        if count == size:
            win = True

    # check columns
    for j in range(size):
        count = 0
        for i in range(size):
            if board[i][j] == player:
                count += 1
        if count == size:
            win = True

    count = 0
    for i in range(size):
        if board[i][i] == player:
            count += 1
    if count == size:
        win = True
    count = 0
    for i in range(size):
        if board[i][size-i-1] == player:
            count += 1
    if count == size:
        win = True
    if win:
        for r in board:
            print(" ".join(r))
        print("Player", player, "wins")
        break

    if player == "X":
        player = "O"
    else:
        player = "X"

if moves == size * size and not win:
    print("Game Draw")
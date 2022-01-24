def checkValidity(board):
    countX = 0
    countO = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                countX += 1
            elif board[i][j] == 'O':
                countO += 1
    if countX + countO <= 5:
        return abs(countX-countO) <= 1
    if abs(countX-countO) > 1:
        return False
    isXWinner = checkWinner(board, 'X')
    isOWinner = checkWinner(board, 'O')
    return not (isOWinner and isXWinner)

def checkWinner(board, player):
    return checkRows(board, player) or checkColumns(board, player) or checkDiagonals(board, player)

def checkRows(board, player):
    return (board[0][0] == player and board[0][1] == player and board[0][2] == player) or (board[1][0] == player and board[1][1] == player and board[1][2] == player) or (board[2][0] == player and board[2][1] == player and board[2][2] == player)

def checkColumns(board, player):
    return (board[0][0] == player and board[1][0] == player and board[2][0] == player) or (board[0][1] == player and board[1][1] == player and board[2][1] == player) or (board[0][2] == player and board[1][2] == player and board[2][2] == player)

def checkDiagonals(board, player):
    return (board[0][0] == player and board[1][1] == player and board[2][2] == player) or (board[0][2] == player and board[1][1] == player and board[2][0] == player)

board = [['X', 'X', 'X'],
       ['O', '-', '-'],
       ['O', 'O', 'X']]

print(checkValidity(board))
# check a given board to see if the game is over
def check_end(board):
    winner = 0

    if board[0] == board[1] and board[1] == board[2] and board[2] != 0:
        winner = board[0]
    if board[3] == board[4] and board[4] == board[5] and board[5] != 0:
        winner = board[3]
    if board[6] == board[7] and board[7] == board[8] and board[8] != 0:
        winner = board[6]
    if board[0] == board[3] and board[3] == board[6] and board[6] != 0:
        winner = board[0]
    if board[1] == board[4] and board[4] == board[7] and board[7] != 0:
        winner = board[1]
    if board[2] == board[5] and board[5] == board[8] and board[8] != 0:
        winner = board[2]
    if board[0] == board[4] and board[4] == board[8] and board[8] != 0:
        winner = board[0]
    if board[2] == board[4] and board[4] == board[6] and board[6] != 0:
        winner = board[2]

    # winner
    if winner != 0:
        return winner
    
    # game is not over
    for i in board:
        if i == 0:
            return 0

    # draw
    return -1
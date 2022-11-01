"""
Tic Tac Toe Player
"""

from math import inf
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():

    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):

    x_count = 0
    o_count = 0

    for r in range(3):
        for c in range(3):
            if board[r][c] == X:
                x_count += 1
            if board[r][c] == O:
                o_count += 1

    if x_count > o_count:
        return O
    else:
        return X


def actions(board):

    possible_actions = set()

    for r in range(3):
        for c in range(3):
            if board[r][c] == EMPTY:
                possible_actions.add((r, c))

    return possible_actions


def result(board, action):

    if action not in actions(board):
        raise Exception(
            "Action not valid -- Space already occupied. Please select new space")

    r, c = action
    copy_board = deepcopy(board)
    copy_board[r][c] = player(board)
    return copy_board


def row_check(board, player):
    for r in range(3):
        if board[r][0] == player and board[r][1] == player and board[r][2] == player:
            return True
    return False


def col_check(board, player):
    for c in range(3):
        if board[0][c] == player and board[1][c] == player and board[2][c] == player:
            return True
    return False


def diag_check(board, player):
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    elif board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    else:
        return False


def winner(board):
    if row_check(board, X) or col_check(board, X) or diag_check(board, X):
        return X
    elif row_check(board, O) or col_check(board, O) or diag_check(board, O):
        return O
    else:
        return EMPTY


def terminal(board):

    if winner(board) == X or winner(board) == O:
        return True
    for r in range(3):
        for c in range(3):
            if board[r][c] == None:
                return False

    return True


def utility(board):
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def max_value(board):

    v = -inf
    if terminal(board):
        return utility(board)

    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):

    v = inf
    if terminal(board):
        return utility(board)

    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v


def minimax(board):
    if terminal(board):
        return EMPTY

    elif player(board) == X:
        all_plays = []
        for action in actions(board):
            all_plays.append([action, min_value(result(board, action))])

        return sorted(all_plays, key=lambda a: a[1])[len(all_plays) - 1][0]

    elif player(board) == O:
        all_plays = []
        for action in actions(board):
            all_plays.append([action, max_value(result(board, action))])

        return sorted(all_plays, key=lambda a: a[1])[0][0]

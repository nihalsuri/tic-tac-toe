"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_freq = 0
    o_freq = 0
    
    x_freq = sum([i.count(X) for i in board])
    o_freq = sum([i.count(O) for i in board])
    
    if x_freq > o_freq : return O
    else : return X
    
    

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    
    for r in range(3):
        for c in range(3): 
            if board[r][c] == EMPTY: 
                possible_actions.add((r , c))
    
    return possible_actions 
        
    


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board): 
        raise Exception("Action not valid -- Space already occupied. Please select new space")
    
    r , c = action 
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
    """
    Returns the winner of the game, if there is one.
    """
    
    if player == X: 
        if row_check(board, player) or col_check(board, player) or diag_check(board, player): 
            return X
    elif player == O: 
        if row_check(board, player) or col_check(board, player) or diag_check(board, player): 
            return O 
    else: 
        return EMPTY
    
    
    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError

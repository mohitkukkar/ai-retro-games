"""
Tic Tac Toe Player
"""

import math
import copy

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
    if board == initial_state():
        return X
    
    moves_x = 0
    moves_o = 0
    
    for row in range(3):
        for column in range(3):
            if board[row][column] == X:
                moves_x += 1
            if board[row][column] == O:
                moves_o += 1
                
    if moves_x > moves_o:
        return O
    else: 
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    available_moves = []
    
    for row in range(3):
        for column in range(3):
            if board[row][column] == EMPTY:
                available_moves.append((row,column))
    return available_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board_copy = copy.deepcopy(board)
    
    try:
        if board_copy[action[0]][action[1]] != EMPTY:
            raise ValueError
        else:
            board_copy[action[0]][action[1]] = player(board)
            
    except ValueError:
        print('Invalid Move')
    
    return board_copy

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    x_actions = []
    o_actions = []
    
    for row in range(3):
        for column in range(3):
            
            if board[row][column] == X:
                x_actions.append((row,column))
                    
            if board[row][column] == O:
                o_actions.append((row,column))
                
    def winner_check(actions_performed):
        
        row = []
        column = []
        diagonal = []
        
        for action in actions_performed:
            row.append(action[0])
            column.append(action[1])
        
            if action[0] == action[1]:
                diagonal.append(1)
                
            if action[0] + action[1] == 2:
                diagonal.append(0)
                
        def win_type(entity):
            is_winner = False
            if len(entity) >= 3:
                for i in range(3):
                    if entity.count(i) == 3:
                        is_winner = True
                        
            return is_winner
        
        if win_type(row):
            return True
        elif win_type(column):
            return True
        elif win_type(diagonal):
            return True
        else:
            return False
        
    if winner_check(x_actions):
        return X
    elif winner_check(o_actions):
        return O
    else:
        return EMPTY

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    Termination = True
    
    if winner(board) == EMPTY:
        for row in range(3):
            for column in range(3):
                if board[row][column] == EMPTY:
                    Termination = False
                    break

    return Termination

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def max_value(board):
        
        if terminal(board):
            beta_value = utility(board)
        else:
            beta_value = -math.inf
            for action in actions(board):
                beta_value = max(beta_value, min_value(result(board, action)))  
                if alpha_value < beta_value:
                    break 

        return beta_value
            
            
    def min_value(board):
        
        if terminal(board):
            beta_value = utility(board)
        else:
            beta_value = math.inf
            for action in actions(board):
                beta_value = min(beta_value, max_value(result(board, action)))   
                if alpha_value > beta_value:
                    break

        return beta_value
    
    if player(board) == X:
        alpha_value = -math.inf
        for action in actions(board):
            beta_value = min_value(result(board, action))
            if beta_value > alpha_value:
                alpha_value = beta_value
                best_action =  action
    else:
        alpha_value = math.inf
        for action in actions(board):
            beta_value = max_value(result(board, action))
            if beta_value < alpha_value:
                alpha_value = beta_value
                best_action =  action

    return best_action

"""
Tic Tac Toe Player
"""
#NAME - Rittik Gupta, Shakia Shahid, Abdalla Ibrahim

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
    Returns the player who has the next turn on the board.
    """
    count_X = sum(row.count('X') for row in board) #finds the sum of x
    count_O = sum(row.count('O') for row in board) # finds the sum of o

    if count_X == count_O: #if they are equal, returns x
        return 'X'
    else:
        return 'O' # or else returns o


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set() #created a set 
    for i in range(len(board)): #for look to see if the board is empty and if it is, then adds i and j to the set. 
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
      # if action is valid or not
    i, j = action 
    if board[i][j] != EMPTY:
        raise ValueError("Invalid action: cell already occupied")

    # a deep copy of the board
    new_board = copy.deepcopy(board)

    # to see whose turn it is next
    current_player = player(board)

    # Apply the action to the new board
    new_board[i][j] = current_player

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != EMPTY:
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    # No winner found
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Check if there's a winner
    if winner(board) is not None:
        return True

    # Check if the board has empty spaces
    for row in board:
        if EMPTY in row:
            return False  # Still empty cells, game not over

    # If no empty cells are found and there's no winner, it's a tie
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_player = winner(board)
    if winner_player == 'X': # returns 1 winner is X
        return 1
    elif winner_player == 'O': #returns O if winner is O
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    if terminal(board): #checking to see if terminal state is running
        return None
    
    current_player = player(board) #assigning player to a new variable
    
    if current_player == 'X': #checking to get the minimum value and finding the better value
        best_value = float('-inf')
        best_action = None
        for action in actions(board):
            value = min_value(result(board, action))
            if value > best_value:
                best_value = value
                best_action = action
    else:  # current_player == O
        best_value = float('inf')
        best_action = None
        for action in actions(board):
            value = max_value(result(board, action))
            if value < best_value:
                best_value = value
                best_action = action

    return best_action


def max_value(board): #checking to see if game is in terminal and if it is, it will return utility(board)
    if terminal(board):
        return utility(board)

    v = float('-inf') #setting the variable to -inf
    for action in actions(board): #for loop to go over all the possibilites
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board): #checking to see if game is in terminal and if it is, it will return utility(board)
    if terminal(board):
        return utility(board)

    v = float('inf') #setting the variable to -inf
    for action in actions(board): #for loop to go over all the possibilites
        v = min(v, max_value(result(board, action)))
    return v
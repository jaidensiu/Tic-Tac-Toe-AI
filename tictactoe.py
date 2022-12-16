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
    numX = 0
    numO = 0

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == X:
                numX += 1
            if board[i][j] == O:
                numO += 1

    if numX > numO:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    allPossibleActions = set()

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == EMPTY:
                allPossibleActions.add((i, j))
    
    return allPossibleActions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Invalid action.")

    boardCopy = copy.deepcopy(board)
    boardCopy[action[0]][action[1]] = player(board)
    
    return boardCopy


def winner(board):
    """
    Returns the winner of the game, if there is one.

    Goes through the rows, columns, and then the two diagonals.
    """
    for i in range(len(board)):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == X:
                return X
            elif board[i][0] == O:
                return O
            else:
                return None

    for j in range(len(board[0])):
        if board[0][j] == board[1][j] == board[2][j]:
            if board[0][j] == X:
                return X
            elif board[0][j] == O:
                return O
            else:
                return None

    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == X:
            return X
        elif board[0][0] == O:
            return O
        else:
            return None

    if board[2][0] == board[1][1] == board[0][2]:
        if board[2][0] == X:
            return X
        elif board[2][0] == O:
            return O
        else:
            return None

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if (winner(board) == X):
        return True
    elif (winner(board) == O):
        return True
        
    for i in range(len(board)):
        for j in range(len(board[0])):
            if  board[i][j] == EMPTY:
                return False

    return True


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
    if terminal(board):
        return None

    if player(board) == X:
        plays = []
        for action in actions(board):
            plays.append([minValue(result(board, action)), action])
        return sorted(plays, key=lambda x: x[0], reverse=True)[0][1]
    elif player(board) == O:
        plays = []
        for action in actions(board):
            plays.append([maxValue(result(board, action)), action])
        return sorted(plays, key=lambda x: x[0], reverse=False)[0][1]


def maxValue(board):
    """
    Helper function for the minimax algorithm.
    """
    v = -math.inf

    if terminal(board):
        return utility(board)

    for action in actions(board):
        v = max(v, minValue(result(board, action)))
    
    return v


def minValue(board):
    """
    Helper function for the minimax algorithm.
    """
    v = math.inf

    if terminal(board):
        return utility(board)

    for action in actions(board):
        v = min(v, maxValue(result(board, action)))
    
    return v
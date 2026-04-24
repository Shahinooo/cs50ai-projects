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
    # X turn when initial state, O turn when X>O so x_count and o_count
    x_count = 0
    o_count = 0
    for row in board:
        for cell in row:
            if cell == X:
                x_count += 1
            elif cell == O:
                o_count += 1

    if x_count > o_count:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_moves = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_moves.add((i, j))

    return possible_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Move is not possible")

    board_copy = copy.deepcopy(board)

    i, j = action
    board_copy[i][j] = player(board)

    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # check for row win
    for i in range(3):
        if board[i][0] == X and board[i][1] == X and board[i][2] == X:
            return X
        elif board[i][0] == O and board[i][1] == O and board[i][2] == O:
            return O

    # checking for columns
    for j in range(3):
        if board[0][j] == X and board[1][j] == X and board[2][j] == X:
            return X
        elif board[0][j] == O and board[1][j] == O and board[2][j] == O:
            return O

    # diagonals
    if (board[0][0] == X and board[1][1] == X and board[2][2] == X) or (board[0][2] == X and board[1][1] == X and board[2][0] == X):
        return X
    elif (board[0][0] == O and board[1][1] == O and board[2][2] == O) or (board[0][2] == O and board[1][1] == O and board[2][0] == O):
        return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    # check for winer
    if winner(board) != None:
        return True

    for row in board:
        for cell in row:
            if cell == EMPTY:
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

    # max value function
    def Max_Value(board):
        max_action = ()
        v = -2
        if terminal(board):
            return utility(board), max_action
        else:
            for action in actions(board):
                if Min_Value(result(board, action))[0] > v:
                    v = Min_Value(result(board, action))[0]
                    max_action = action
            return v, max_action

    def Min_Value(board):
        min_action = ()
        v = 2
        if terminal(board):
            return utility(board), min_action
        else:
            for action in actions(board):
                if Max_Value(result(board, action))[0] < v:
                    v = Max_Value(result(board, action))[0]
                    min_action = action
            return v, min_action

    if terminal(board):
        return None

    elif player(board) == X:
        return Max_Value(board)[1]

    elif player(board) == O:
        return Min_Value(board)[1]

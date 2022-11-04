"""
Tic Tac Toe Player
"""
from copy import deepcopy
import math

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

#this function returns who's turn it is, if the state is terminal it can return either player
def player(board):
    """
    Returns player who has the next turn on a board.
    """
    #check if state is terminal, if yes return either
    if terminal(board):
        return "Game is over"
    
    #if not return who's move it is
    #will be used to add totals of each type 
    totalX = 0
    totalO = 0

    #deciding player turn
    for obj in board:
        totalX  = totalX + obj.count(X)
        totalO  = totalO + obj.count(O)

    #if #X=#O then it is X turn, if not then it is O turn
    if totalX==totalO:
        return X
    elif totalO!=totalX:
        return O    
    
    #raise NotImplementedError

#given board, return all possible actions to take, #if terminal board then any move is accepted
def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    #first you should check is a state is terminal 
    if terminal(board):
        return "Game is over"

    #empty set that will later store result
    s=set()
    #loop through all possibilities, whenever something is empty, pull its oordinates, and add it to set
    for i in range(0,len(board)):
        for j in range(0,len(board[i])):
            if board[i][j]==EMPTY:
                s.add((i,j))
    
    #return a set of all possible actions
    return s
    #raise NotImplementedError

# returns new board given old board and an action
def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    #raise exception if action is not valid, targets spot that is not empty
    if board[action[0]][action[1] ] is not EMPTY:
        raise NameError(f"The space selected is not empty")

    #Don't just update the board, you have to use a deep copy for some reason, look further into why
    new_board = deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board
    #raise NotImplementedError

#returns the winner if there is one.
def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #return X or O based on winner
    #we can never have two winners
    #if no winner return none

    #looping through rows

    for i in range(0,3):
        if board[i][0]==board[i][1]==board[i][2]:
            if board[i][0]==X:
                return X
            elif board[i][0]==O:
                return O
            else: 
                return None
    #looping through columns:

    for j in range(0,3):
        if board[0][j]==board[1][j]==board[2][j]:
            if board[0][j]==X:
                return X
            elif board[0][j]==O:
                return O
            else:
                return None

    #looping through first diag
    
    if board[0][0]==board[1][1]==board[2][2]:
        if board[0][0]==X:
            return X
        elif board[0][0]==O:
            return O
        else:
            return None
    #looping through second diag
    if board[0][2]==board[1][1]==board[2][0]:
        if board[0][2]==X:
            return X
        elif board[0][2]==O:
            return O
        else:
            return None
    #no winners
    return None
    #raise NotImplementedError

#returns true if game is over, false otherwise
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #check if there is a winner
    if winner(board):
        return True
    #check for a draw (meaning no empty spots in function)
    for i in board:
        for j in i:
            if j==EMPTY:
                return False
    return True
    #raise NotImplementedError

#returns utility of the board
def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):#function will return a value only if board is terminal
        if winner(board)==X:
            return 1
        elif winner(board)==O:
            return -1
        else:
            return 0
    #raise NotImplementedError

#returns optimal move for current player, note we have maximazing player and minimizing player
def minimax(board):
    
    if terminal(board):
        return None

    def max_value(board):
        if terminal(board):
            return utility(board)
        v = float('-inf')
        for action in actions(board):
            v = max(v, min_value(result(board, action)))
        return v
            

    def min_value(board):
        if terminal(board):
            return utility(board)
        v = float('inf')
        for action in actions(board):
            v = min(v, max_value(result(board, action)))
        return v
            

    
    if player(board)==X:
        arr = []
        for action in actions(board):
            arr.append([min_value(result(board,action)), action])
        return sorted(arr, key=lambda x: x[0], reverse=True)[0][1]
            
    elif player(board)==O:
        arr=[]
        for action in actions(board):
            arr.append([max_value(result(board,action)), action])
        return sorted(arr, key=lambda x: x[0])[0][1]
    """
    Returns the optimal action for the current player on the board.
    """
    #returns (i,j)coordinates of the optimal move, if many moves return any of them, if board is termianl return None
    #raise NotImplementedError

import copy 
import game
from math import inf as infinity

'''
def nextMove(grid, symbole):
    if(game.gridFull(grid)): return 0
        
    # Check if game has a winner
    align, sym = game.alignement(grid)
    if(align):
        if(sym == symbole):
            return 1
        else:
            return -1

    temp = grid.copy()

    move = -1
    score = -2

    for row in temp:
        for cell in row:
            # Cell is free
            if cell == None:
                # Make the move
                cell = symbole
                # Count negative score for oponnent
                scoreForTheMove = -nextMove(temp, getOpponentSymbole(symbole))
                if scoreForTheMove > score:
                    score = scoreForTheMove
                    move += 1
    if move == 0:
        return 0
    else:
        return score
'''

def nextMove(state, depth, player):
    bestMove = None
    for cell in game.empty_cells(state):
        cell = player
        move_score = minimax(state, depth, player)
        cell = None
        if(move_score > bestMove):
            bestMove = cell
    return bestMove

def minimax(state, depth, player):
    val, winner = game.alignement(state)
    score = 0
    if(val):
        if(winner == "O"):
            score = +10
        elif(winner == "X"):
            score = -10
    if(game.gridFull(state)):
        score = 0
    
    if(player == "O"): player = "X"
    elif(player == "X"): player = "O"

    best = -1000

    for cell in game.empty_cells(state):
        cell = player
        best = max(best, minimax(state, depth-1, player))
        cell = None

    return best

    
def getOpponentSymbole(sym):
    if(sym == 'O'):
        return 'X'
    elif(sym == 'X'):
        return 'O'

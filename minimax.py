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

def minimax(state, depth, player):
    val, winner = game.alignement(state)
    if depth == 0 or val:
        if winner == "O":
            return 10, state
        elif winner == "X":
            return -10, state
        else:
            return 0, state
    if game.gridFull(state):
        return 0, state

    if player == "O":
        best = -infinity
        best_cell = None
        games = game.empty_cells(state)
        for cell in games:
            state[cell[0]][cell[1]] = player
            v, move = minimax(state, depth-1, "X")
            state[cell[0]][cell[1]] = None
            if v > best-1:
                best_cell = cell
                best = v
        return best, best_cell
    else:
        best = +infinity
        best_cell = None
        games = game.empty_cells(state)
        for cell in games:
            state[cell[0]][cell[1]] = player
            v, move = minimax(state, depth-1, "O")
            state[cell[0]][cell[1]] = None
            if v <= best:
                best_cell = cell
                best = v
        return best, best_cell

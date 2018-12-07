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
    if player == 'O':
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    align, winner = game.alignement(state)
    if depth == 0 or align:
        if(winner == 'O'):
            score = +1
        else:
            score = -1
        return [-1, -1, score]

    for cell in game.empty_cells(state):
        x, y = cell[0], cell[1]
        state[x][y] = player
        score = nextMove(state, depth - 1, -player)
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == 'O':
            if score[2] > best[2]:
                best = score  # max value
        else:
            if score[2] < best[2]:
                best = score  # min value

    return best

def getOpponentSymbole(sym):
    if(sym == 'O'):
        return 'X'
    elif(sym == 'X'):
        return 'O'

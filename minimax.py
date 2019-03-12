import copy 
import game
from math import inf as infinity

def minimax(state, depth, player):
    val, winner = game.alignement(state)
    if depth == 0 or val:
        if winner == "O":
            return 10, state
        elif winner == "X":
            return -10, state
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
    
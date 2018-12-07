import numpy as np
import random

class Grid():
    def __init__(self):
        self.grid = np.full((3,3), None)

    def __str__(self):
        grid = "["
        for i, cell in enumerate(self.grid):
            if(i == 2 or i == 5):
                grid += " " + str(cell) + " ]\n"
            if(i == 3 or i == 6):
                grid += "[ " + str(cell)
            else:
                grid += " " + str(cell)
        grid += " ]" 
        return grid

class Player():
    def __init__(self, name, symbole):
        self.name = name
        self.symbole = symbole
        self.won_games = 0
        self.draw_games = 0

def gameLoop(p1, p2):

    # Initiliaze the Grid
    grid = Grid()

    # Choose randomly a player
    playerTurn = random.randint(1, 2)


if __name__ == "__main__":
    # Create players
    p1 = Player("vic", "X")
    p2 = Player("sme", "O")

    # Start the game loop
    gameLoop(p1, p2)

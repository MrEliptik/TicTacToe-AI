import numpy as np
import random
import re

class Grid():
    def __init__(self):
        self.grid = np.full((3,3), None)

    def update(self, x, y, symbol):
        if(self.grid[x][y] == None):
            self.grid[x][y] = symbol
            return True
        else:
            print("Cell already used!")
            return False

    def __str__(self):
        grid = ""
        for i, cell in enumerate(self.grid):
            grid += " " + str(cell) + "\n"
        return grid

class Player():
    def __init__(self, name, symbole):
        self.name = name
        self.symbole = symbole
        self.won_games = 0
        self.draw_games = 0
    
    def stat(self):
        return str(self.name + "won " + self.won_games + " games, " + self.draw_games + " draw.")
    
    def __str__(self):
        return self.name

def alignement(grid):
    if(    grid[0][0]==grid[0][1]==grid[0][2] != None #vertical
        or grid[1][0]==grid[1][1]==grid[1][2] != None #vertical
        or grid[2][0]==grid[2][1]==grid[2][2] != None #vertical

        or grid[0][0]==grid[1][0]==grid[2][0] != None #horizontal
        or grid[0][1]==grid[1][1]==grid[2][1] != None #horizontal
        or grid[0][2]==grid[1][2]==grid[2][2] != None #horizontal

        or grid[0][0]==grid[1][1]==grid[2][2] != None #diagonal
        or grid[1][1]==grid[0][2]==grid[2][0] != None #diagonal
    ): 
        return True
    else:
        return False

def gridFull(grid):
    for rows in grid:
        for cell in rows:
            if cell == None:
                return False
    return True

def gameLoop(p1, p2):

    def getPlayerInput():
        print("{} next move : x y (0 < x y < 2)".format(playerTurn))
        x = '-1'
        y = '-1'
        while((int(x) < 0 or int(x) > 2) or (int(y) < 0 or int(y) > 2)):
            location = input()
            x, y = re.split(' ', location)
            if(int(x) >= 0 and int(x) < 3 and int(y) >= 0 and int(y) < 3):
                return int(x), int(y)
            else:
                print("Location not valid!\n Must be : x y with 0 < x y < 2")

    def switchPlayer(turn):
        if(turn == p1):
            return p2
        else:
            return p1

    # Initiliaze the Grid
    grid = Grid()

    # Choose randomly a player
    if(random.randint(1, 2) == 1):
        playerTurn = p1
    else:
        playerTurn = p2
    
    # Display the grid
    print(grid)

    # Player place its symbol
    x, y = getPlayerInput()
    while(not grid.update(x, y, playerTurn.symbole)):
        x, y = getPlayerInput()
    
    print(grid)

    while(not alignement(grid.grid) and not gridFull(grid.grid)):
        # Switch player
        playerTurn = switchPlayer(playerTurn)

        # Get player input
        x, y = getPlayerInput()
        while(not grid.update(x, y, playerTurn.symbole)):
            x, y = getPlayerInput()

        # Display the grid
        print(grid)

    if(alignement(grid.grid)):
        playerTurn.won_games += 1
        print("{} won!".format(playerTurn.name))
    elif(gridFull(grid.grid)):
        p1.draw_games += 1
        p2.draw_games += 1
        print("Grid full, draw!")


if __name__ == "__main__":
    # Create players
    p1 = Player("vic", "X")
    p2 = Player("sme", "O")

    inpt = "y"
    while(inpt != "n"):
        # Start the game loop
        gameLoop(p1, p2)

        print(p1.stat())
        print(p2.stat())

        print("New game? y/n")
        inpt = input() 

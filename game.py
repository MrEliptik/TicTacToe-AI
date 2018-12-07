import numpy as np
import random
import re
import minimax as ai

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

    def isMoveAllowed(self, x, y):
        if(self.grid[x][y] == None):
            return True
        else:
            return False

    def __str__(self):
        grid = ""
        for i, row in enumerate(self.grid):
            grid += "|"
            for j, cell in enumerate(row): 
                if(cell == None):
                    grid += " -"
                else:
                    grid += " " + self.grid[i][j]
            grid += " |\n"
        return grid

class Player():
    def __init__(self, name, symbole, isAI=False):
        self.name = name
        self.symbole = symbole
        self.isAI = isAI
        self.won_games = 0
        self.draw_games = 0
    
    def stat(self):
        return self.name + " won " + str(self.won_games) + " games, " + str(self.draw_games) + " draw."
    
    def __str__(self):
        return self.name

def alignement(grid):
    if(grid[0][0] == grid[0][1] == grid[0][2] != None):  # vertical
         return True, grid[0][0]
    elif(grid[1][0] == grid[1][1] == grid[1][2] != None):  # vertical
        return True, grid[1][0]
    elif(grid[2][0] == grid[2][1] == grid[2][2] != None):  # vertical
        return True, grid[2][0]
    elif(grid[0][0] == grid[1][0] == grid[2][0] != None):  # horizontal
        return True, grid[0][0]
    elif(grid[0][1] == grid[1][1] == grid[2][1] != None):  # horizontal
        return True, grid[0][1] 
    elif(grid[0][2] == grid[1][2] == grid[2][2] != None):  # horizontal
        return True, grid[0][2]  
    elif(grid[0][0] == grid[1][1] == grid[2][2] != None):  # diagonal
        return True, grid[0][0]
    elif(grid[1][1] == grid[0][2] == grid[2][0] != None):  # diagonal
        return True, grid[1][1]
    else:
        return False, None

def gridFull(grid):
    for rows in grid:
        for cell in rows:
            if cell == None:
                return False
    return True


def empty_cells(state):
    cells = []

    for y, row in enumerate(state):
        for x, cell in enumerate(row):
            if cell == None:
                cells.append([x, y])
    #print(cells)
    return cells

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

    # Check if player is AI
    if(playerTurn.isAI):
            depth = len(empty_cells(grid.grid))
            if depth == 0:
                return
            if depth == 9:
                x = random.randint(0, 2)
                y = random.randint(0, 2)
            else:
                move = ai.nextMove(grid.grid.copy(), depth, playerTurn.symbole)
                x, y = move[0], move[1]
            grid.update(x, y, playerTurn.symbole)
            
    else:
        # Player place its symbol
        x, y = getPlayerInput()
        while(not grid.update(x, y, playerTurn.symbole)):
            x, y = getPlayerInput()
    
    print(grid)
    aligned, _ = alignement(grid.grid)
    while(not aligned and not gridFull(grid.grid)):
        # Switch player
        playerTurn = switchPlayer(playerTurn)

        # Check if player is AI
        if(playerTurn.isAI):
            depth = len(empty_cells(grid.grid))
            if depth == 0:
                return
            if depth == 9:
                x = random.randint(0, 2)
                y = random.randint(0, 2)
            else:
                move = ai.nextMove(grid.grid.copy(), depth, playerTurn.symbole)
                x, y = move[0], move[1]
            grid.update(x, y, playerTurn.symbole)
        else:
            # Get player input
            x, y = getPlayerInput()
            while(not grid.update(x, y, playerTurn.symbole)):
                x, y = getPlayerInput()

        # Display the grid
        print(grid)

        # Check if there's a winner
        aligned, _ = alignement(grid.grid)

    if(alignement(grid.grid)):
        playerTurn.won_games += 1
        print("{} won!".format(playerTurn.name))
    elif(gridFull(grid.grid)):
        p1.draw_games += 1
        p2.draw_games += 1
        print("Grid full, draw!")


if __name__ == "__main__":
    # Create players
    p1 = Player("vic", "X", isAI=False)
    p2 = Player("AI", "O", isAI=True)

    inpt = "y"
    while(inpt != "n"):
        # Start the game loop
        gameLoop(p1, p2)

        print(p1.stat())
        print(p2.stat())

        print("New game? y/n")
        inpt = input() 

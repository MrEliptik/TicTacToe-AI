import numpy as np
import random
import minimax as ai
import gui

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
    if(grid[0][0] == grid[0][1] == grid[0][2] != None):  # horizontal
         return True, grid[0][0]
    elif(grid[1][0] == grid[1][1] == grid[1][2] != None):  # horizontal
        return True, grid[1][0]
    elif(grid[2][0] == grid[2][1] == grid[2][2] != None):  # horizontal
        return True, grid[2][0]
    elif(grid[0][0] == grid[1][0] == grid[2][0] != None):  # vertical
        return True, grid[0][0]
    elif(grid[0][1] == grid[1][1] == grid[2][1] != None):  # vertical
        return True, grid[0][1] 
    elif(grid[0][2] == grid[1][2] == grid[2][2] != None):  # vertical
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

    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if cell == None:
                cells.append([x, y])
    #print(cells)
    return cells

def gameLoop(screen, p1, p2):

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

    # Check if player is AI
    if(playerTurn.isAI):
            depth = len(empty_cells(grid.grid))
            if depth == 0:
                return
            if depth == 9:
                x = random.randint(0, 2)
                y = random.randint(0, 2)
            else:
                _, move = ai.minimax(grid.grid, depth, playerTurn.symbole)
                x, y = move[0], move[1]
            grid.update(x, y, playerTurn.symbole)
            gui.drawSymbole(screen, (x, y), playerTurn.symbole)
            
    else:
        # Player place its symbol
        x, y = gui.input(screen)
        grid.update(x, y, playerTurn.symbole)
        gui.drawSymbole(screen, (x, y), playerTurn.symbole)
    
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
                score, move = ai.minimax(grid.grid, depth, playerTurn.symbole)
                x, y = move[0], move[1]
            grid.update(x, y, playerTurn.symbole)
            gui.drawSymbole(screen, (x,y), playerTurn.symbole)
        else:
            # Get player input
            x, y = gui.input(screen)
            grid.update(x, y, playerTurn.symbole)
            gui.drawSymbole(screen, (x, y), playerTurn.symbole)

        # Check if there's a winner
        aligned, _ = alignement(grid.grid)

    if(aligned):
        playerTurn.won_games += 1
        return playerTurn
        
    elif(gridFull(grid.grid)):
        p1.draw_games += 1
        p2.draw_games += 1
        return 0

if __name__ == "__main__":
    inpt = "y"
    p1 = Player("vic", "X")
    p2 = Player("AI", "O", isAI=True)
    screen = gui.init()

    while(inpt != "n"):    
        
        # Start the game loop
        winner = gameLoop(screen, p1, p2)

        if(winner != 0):
            gui.writeScreen(screen, winner.name + " won!")          
        else:           
            gui.writeScreen(screen, "Draw!", line=1)
            
        gui.writeScreen(screen, "Click to", line=2)
        gui.ask(screen, " play again!", line=3)
        gui.clearScreen(screen)
        print(p1.stat())
        print(p2.stat())
        

import sys
import pygame

WHITE = 255, 255, 255
BLACK = 0, 0, 0
size = width, height = 480, 480

def init():
    pygame.init()
    screen = pygame.display.set_mode(size)
    screen.fill(WHITE)

    # Horizontal lines
    for i in range(1, 3):
        pygame.draw.line(screen, BLACK, [0, (height/3)*i], [width, ((height/3)*i)], 3)
    # Vertical lines
    for i in range(1, 3):
        pygame.draw.line(screen, BLACK, [(width/3)*i, 0], [((width/3)*i), height], 3)
    
    return screen

def getCell(pos):
    if(pos[0] >= 0 and pos[0] < width/3 and pos[1] >= 0 and pos[1] < height/3):
        return (0, 0)
    if(pos[0] >= width/3 and pos[0] < (width/3)*2 and pos[1] >= 0 and pos[1] < height/3):
        return (0, 1)
    if(pos[0] >= (width/3)*2 and pos[0] < width and pos[1] >= 0 and pos[1] < height/3):
        return (0, 2)
    if(pos[0] >= 0 and pos[0] < width/3 and pos[1] >= height/3 and pos[1] < (height/3)*2):
        return (1, 0)
    if(pos[0] >= width/3 and pos[0] < (width/3)*2 and pos[1] >= height/3 and pos[1] < (height/3)*2):
        return (1, 1)
    if(pos[0] >= (width/3)*2 and pos[0] < width and pos[1] >= height/3 and pos[1] < (height/3)*2):
        return (1, 2)
    if(pos[0] >= 0 and pos[0] < width/3 and pos[1] >= (height/3)*2 and pos[1] < height):
        return (2, 0)
    if(pos[0] >= width/3 and pos[0] < (width/3)*2 and pos[1] >= (height/3)*2 and pos[1] < height):
        return (2, 1)
    if(pos[0] >= (width/3)*2 and pos[0] < width and pos[1] >= (height/3)*2 and pos[1] < height):
        return (2, 2)

def drawSymbole(screen, cell, symbole):
    if(symbole == "X"):
        pass
    elif(symbole == "O"):
        pygame.draw.circle(screen, BLACK, (int(cell[0]/2), int(cell[1]/2)), int((width/3)*0.9), 1)

def gameLoop(screen):
    while 1:
        for event in pygame.event.get():
            # handle MOUSEBUTTONUP
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                cell = getCell(pos)
                #drawSymbole(screen, cell, "O")

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            pygame.display.update()

if __name__ == "__main__":
    screen = init()
    gameLoop(screen)

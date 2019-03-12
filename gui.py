import sys
import pygame
from math import sqrt as sqrt

import time

WHITE = 255, 255, 255
BLACK = 0, 0, 0
size = width, height = 480, 480
cell_width = (width/3)
cell_height = (height/3)
font_size = 60

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

def clearScreen(screen):
    screen.fill(WHITE)

    # Horizontal lines
    for i in range(1, 3):
        pygame.draw.line(
            screen, BLACK, [0, (height/3)*i], [width, ((height/3)*i)], 3)
    # Vertical lines
    for i in range(1, 3):
        pygame.draw.line(
            screen, BLACK, [(width/3)*i, 0], [((width/3)*i), height], 3)


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
        x00 = int(((width/3)*cell[1]))
        y00 = int(((height/3)*cell[0]))
        x01 = int(((width/3)*cell[1]) + cell_width)
        y01 = int(((height/3)*cell[0]) + cell_height)

        x10 = int(((width/3)*cell[1]) + cell_width)
        y10 = int(((height/3)*cell[0]))
        x11 = int(((width/3)*cell[1]))
        y11 = int(((height/3)*cell[0]) + cell_height)
        pygame.draw.line(screen, BLACK, (x00, y00), (x01, y01), 1)
        pygame.draw.line(screen, BLACK, (x10, y10), (x11, y11), 1)
    elif(symbole == "O"):
        # Cell[1] for x because it doesn't change on
        # the line
        x = int(((width/3)*cell[1]) + cell_width/2)
        y = int(((height/3)*cell[0]) + cell_height/2)
        pygame.draw.circle(screen, BLACK, (x, y), int((width/3/2)*0.9), 1)
    
    refresh()

def playerInput(screen):
    running = True
    while running:
        for event in pygame.event.get():
            # handle MOUSEBUTTONUP
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                cell = getCell(pos)
                return cell[0], cell[1]
            if event.type == pygame.QUIT:
                running = False
            refresh()
    pygame.quit()  # quits pygame
    sys.exit()

def ask(screen, question, line=2):
    running = True
    # "ask(screen, question) -> answer"
    pygame.font.init()
    writeScreen(screen, question, line=line)
    center_yes_x = width/4
    center_yes_y = height/4
    center_no_x = (width/4)*2
    center_no_y = (height/4)
    while running:
        for event in pygame.event.get():
            # handle MOUSEBUTTONUP
            if event.type == pygame.MOUSEBUTTONUP:
                return
            if event.type == pygame.QUIT:
                running = False
            refresh()
    pygame.quit()
    sys.exit()

def writeScreen(screen, txt, line=1):
    # initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
    myfont = pygame.font.SysFont("monospace", font_size)

    # render text
    label = myfont.render(txt, 50, (0,200,0))
    screen.blit(label, ((width/2)-(font_size/3)*len(txt), (height/4)*line))
    refresh()

def refresh():
    pygame.display.update()
    
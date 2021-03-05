# Eka peli 0.3
#
#
# platformer made with pygame
import pygame
from pygame.locals import *
from config.py import *
from classes.py import *
import random
import sys     # sys-module will be needed to exit the program

pygame.init()
windowGame =  pygame.display.set_mode((windowWidth,windowWidth))
pygame.display.set_caption("D4 gäng")
# Load static images



#   function for easier visualisation
#   draws a grid for tiles
def drawGrid():
    for line in range(0,11):
        pygame.draw.line(windowGame, (255,255,255), (0, line * tileSize), (windowWidth, line * tileSize))
        pygame.draw.line(windowGame, (255,255,255), (line * tileSize, 0), (line * tileSize, windowHeight))



#   create hero pelaaja and the world
player = Player(100, windowHeight - 150, 1, 1, [])
world = World(worldDataGrid)




run=True    #   set running to true
while run:

    FPS.tick(100)                # FPS clock tick rate 100
    
    # check if the user has closed the display-window or pressed esc
    for event in pygame.event.get():  # all the events in the event queue
        if event.type == pygame.QUIT: # if the player closed the window
            pygame.quit() # the display-window closes
            sys.exit()    # the whole python program exits

        if event.type == KEYDOWN:     # if the player pressed down any key
            if event.key == K_ESCAPE: # if the key was esc
                pygame.quit() # the display-window closes
                sys.exit()    # the whole python program exits








    # clear the display-surface and draw all the Surfaces again
    windowGame.blit(tausta, (0,0)) # without this, moving characters would have a "trace"
    world.draw()
    drawGrid()
    player.update()
    
    pygame.display.update()
    

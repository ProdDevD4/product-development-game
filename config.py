import pygame

FPS = pygame.time.Clock()   #   clock for our tic rate

# colours
black = pygame.Color(0, 0, 0)         # Black

white = pygame.Color(255, 255, 255)   # White

grey = pygame.Color(128, 128, 128)   # Grey

red = pygame.Color(255, 0, 0)       # Red

orange = pygame.Color(255, 165, 0)   #Orange

#   create window and set tile size
windowWidth = 900
windowHeight = 900
windowGame =  pygame.display.set_mode((windowWidth,windowWidth))
pygame.display.set_caption("D4 gäng")
tileSize = 90
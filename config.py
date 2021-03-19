    import pygame

FPS = pygame.time.Clock()   #   clock for our tic rate

# colours
black = pygame.Color(0, 0, 0)         # Black

white = pygame.Color(255, 255, 255)   # White

grey = pygame.Color(128, 128, 128)   # Grey

red = pygame.Color(255, 0, 0)       # Red

orange = pygame.Color(255, 165, 0)   #Orange



        
#load images
sandImg = pygame.image.load("img/sand.png")
grassImg = pygame.image.load("img/grass.png")
#stoneImg = pygame.image.load("img/stoneBlock.png")
duck = pygame.image.load("img/duck_idle.png")
#   create window and set tile size
windowWidth = 960
windowHeight = 960
tileSize = 36




worldDataGrid = [
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[2, 0, 0, 0, 1, 1, 1, 0, 0, 2], 
[0, 2, 0, 0, 0, 0, 0, 0, 2, 0], 
[0, 0, 2, 0, 0, 0, 0, 2, 0, 0],
[0, 0, 0, 2, 0, 0, 2, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 2, 0, 0, 0, 2, 0],
[0, 0, 0, 2, 0, 0, 1, 0, 0, 0],
[0, 0, 2, 0, 0, 0, 1, 0, 0, 0], 
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

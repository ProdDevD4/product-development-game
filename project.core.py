# Eka peli 0.3
#
#
# platformer made with pygame
import pygame
from pygame.locals import * 
import random
import sys     # sys-module will be needed to exit the program

pygame.init()

FPS = pygame.time.Clock()   #   clock for our tic rate

# colours
black = pygame.Color(0, 0, 0)         # Black

white = pygame.Color(255, 255, 255)   # White

grey = pygame.Color(128, 128, 128)   # Grey

red = pygame.Color(255, 0, 0)       # Red

orange = pygame.Color(255, 165, 0)   #Orange

#   create window and set tile size
windowWidth = 1000
windowHeight = 1000
windowGame =  pygame.display.set_mode((windowWidth,windowWidth))
pygame.display.set_caption("D4 gäng")
tileSize = 30

# Load static images



# pallo = pygame.image.load("img/#kivi.png").convert_alpha() 
tausta = pygame.image.load("img/tausta.png")
#ikkuna.blit(tausta, (0,0))
#kelluva = pygame.image.load("img/kelluu.png")

class World():                #   Class to construct our world
    def __init__(self, data):    #   Constructor that takes world data as local variable
        self.tileList = []
#        maa = pygame.image.load("img/maa.png")
#        kelluva = pygame.image.load("img/kelluu.png")
        rowCount = 0           #   start at row 0
        for row in data:       #   for loop to iterate through maailma_data and set images accordingly
            columnCount = 0       #   start at column 0
            for tile in row:
                if tile == 0:
                    img = pygame.transform.scale(pygame.image.load("img/Blocks/sandBlock.png").convert_alpha(), (tileSize, tileSize))
                    imgRect = img.get_rect()
                    imgRectX = columnCount * tileSize        
                    imgRectY = rowCount * tileSize
                    tile = (img, imgRect)              #   tuple to hold tile image and coordinates
                    self.tileList.append(tile)        #   append tile to tile list
                if tile == 1:   #   1 = ground
                    img = pygame.transform.scale(pygame.image.load("img/Blocks/dirtBlock.png").convert_alpha(), (tileSize, tileSize))
                    imgRect = img.get_rect()
                    imgRectX = columnCount * tileSize        
                    imgRectY = rowCount * tileSize
                    tile = (img, imgRect)              #   tuple to hold tile image and coordinates
                    self.tileList.append(tile)        #   append tile to tile list
                if tile == 2:   #   2 = floating ground
                    img = pygame.transform.scale(pygame.image.load("img/Blocks/stoneBlock.png").convert_alpha(), (tileSize, tileSize))
                    imgRect = img.get_rect()
                    imgRectX = columnCount * tileSize
                    imgRectY = rowCount * tileSize
                    tile = (img, imgRect)
                    self.tileList.append(tile)
                columnCount += 1 #   next column
            rowCount += 1     #   next row

    def draw(self):
        for tile in self.tileList:        #   iterate through tile list and blit them on screen
            windowGame.blit(tile[0], tile[1])


class Player():                                               #   create Class called Pelaaja
    def __init__(self, x, y, lvl, area, inventory):                                   #   constructor that takes x and y coordinates as local variables
        img = pygame.image.load("img/hero.png").convert_alpha() #   set the picture
        self.bitmap = pygame.transform.scale(img, (35, 50))
        self.rect = self.bitmap.get_rect()                        #   get outlines of hero for collisions
        self.rect.x = x
        self.rect.y = y
        self.playerWidth = self.bitmap.get_width()
        self.playerHeight = self.bitmap.get_height()
        self.ySpeed = 0
        self.xSpeed = 0   
        self.dash = False
        self.lvl = lvl
        self.area = area
        self.inventory = inventory
    
    def levelUp(self):
        lvl += 1
    
    
    def update(self):   #   function to update hero's position
        deltaX = 0
        deltaY = 0

        pressedKeys = pygame.key.get_pressed()    #    get.pressed()-function gives a list of all the keys that are being pressed
        if pressedKeys[K_LEFT]:                   #    check key presses for direction of movement
            deltaX -= 3                            #    save where hero would end up but don't move hero yet for collision detecting purposes
        if pressedKeys[K_RIGHT]:
            deltaX += 3
        if pressedKeys[K_UP]:
            deltaY += -3
        if pressedKeys[K_DOWN]:
            deltaY += 3
        
        
        #   collision testing
        for tile in world.tileList:
            
            #   x collision
            if tile[1].colliderect(self.rect.x + deltaX, self.rect.y, self.playerWidth, self.playerHeight):   #   if we bump into anything simply stop
                deltaX = 0
            
            
            #   y collision
            if tile[1].colliderect(self.rect.x, self.rect.y + deltaY, self.playerWidth, self.playerHeight):
                deltaY = 0                        #   set jump to False after touching a surface
                    
        self.rect.x += deltaX        #   deltas have been checked so we add them to the actual coordinates   
        self.rect.y += deltaY
        windowGame.blit(self.bitmap, self.rect)
        
"""
class Enemy(self, type):
    def __init__(self, x, y):
        img =  pygame.image.load("img/kivi.png").convert_alpha() 
        self.bitmap = pygame.transform.scale(img (50, 50))
        self.rect = self.bitmap.get_rect()
        self.rect.x = x
        self.rect.y = y
"""

#   function for easier visualisation
#   draws a grid for tiles
def drawGrid():
    for line in range(0,11):
        pygame.draw.line(windowGame, (255,255,255), (0, line * tileSize), (windowWidth, line * tileSize))
        pygame.draw.line(windowGame, (255,255,255), (line * tileSize, 0), (line * tileSize, windowHeight))


#   this list contains lists of tile types per tile
#   0 = nothing
#   1 = ground
#   2 = floating ground


#with open('input.txt', 'r') as f:
    
        #jos on tyhjiä rivejä ni tää mut ei meil oo
    
    #maailma_data = [[int(num) for num in line.split(' ,')] for line in f if line.strip() = "/n" ]
   # maailma_data = [[int(num) for num in line.split(',')] for line in f]
#print (maailma_data)

worldDataGrid = [
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,2,3,3,3,3,3,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,2,3,3,3,2,3,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,2,3,3,3,2,3,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,2,3,2,2,2,3,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,2,3,3,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,2,3,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,2,3,3,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,2,3,3,3,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,2,2,3,3,3,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,0,2,3,3,3,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,0,2,2,2,3,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,0,0,0,2,3,3,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,0,0,0,2,3,3,3,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,0,0,0,2,2,3,3,3,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,0,0,0,0,2,3,3,3,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,0,0,0,0,2,2,2,3,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,2,3,3,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,2,3,3,3,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,2,2,3,3,3,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,0,2,3,3,3,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,0,2,2,2,3,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,0,0,0,2,3,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,0,0,0,2,3,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,0,0,2,2,2,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,0,0,2,3,3,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,0,0,2,3,3,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,0,0,2,3,3,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,0,0,2,3,3,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,0,0,2,3,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,0,0,2,3,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,0,0,2,3,3,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,0,0,2,3,3,3,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,0,0,2,2,3,3,3,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,0,0,0,2,3,3,3,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,0,0,0,2,2,2,3,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,0,0,0,0,0,2,3,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,0,0,0,0,0,2,2,2,2,2,0,2,3,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,0,0,0,2,2,2,3,3,3,2,2,2,2,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,0,0,0,2,3,3,3,3,3,2,2,3,3,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,0,0,2,2,3,3,3,2,2,2,2,3,3,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,0,0,2,3,3,3,3,2,2,3,3,3,3,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,0,0,2,3,3,2,2,2,2,3,3,3,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,0,0,2,3,2,2,2,3,3,3,3,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,0,0,2,3,3,3,2,3,3,3,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,0,0,2,3,3,3,3,3,3,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,0,0,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

]

#[
#[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#[2, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
#[0, 2, 0, 0, 0, 0, 0, 0, 2, 0], 
#[0, 0, 2, 0, 0, 0, 0, 2, 0, 0],
#[0, 0, 0, 2, 0, 0, 2, 0, 0, 0],
#[0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
#[0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
#[0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
#[0, 0, 2, 0, 0, 0, 0, 0, 0, 0], 
#[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
#]

#   create hero pelaaja and the world
player = Player(100, windowHeight - 150, 1, 1, [])
world = World(worldDataGrid)

# Event()-function will create an Event-object of a given type
# pygame.USEREVENT = 32847 is preferable type
# if you need more events, use pygame.USEREVENT+1, pygame.USEREVENT+2, etc.
pisteTapahtuma = pygame.event.Event(pygame.USEREVENT)


# the following timer will be used to create collectable balls
# set_timer() will put pisteTapahtuma into the event queue every 2 seconds
# pygame uses milliseconds for tracking time, the 2000 is milliseconds
pygame.time.set_timer(pisteTapahtuma,2000)


# the following lists are used for generating new collectable balls
palloLista = []
koordLista = []
nopeusLista = []


pisteet=0 # variable that keeps tracking the points
nopeus2 = [random.randint(1,5),random.randint(1,5)] # the speed of the collectable balls
kello = pygame.time.Clock() # Clock-object is used to set the frame rate


# font-module can be used to create text into the game
# pygame.font.get_fonts() will give you all the available fonts
fonttiLoppu = pygame.font.SysFont('arial', 90)
fonttiPisteet = pygame.font.SysFont('cambria', 40)
# render()-function will create Surface-object from the text
loppuTeksti = fonttiLoppu.render('GAME OVER', True, red)
pisteTeksti = fonttiPisteet.render('Pisteet: '+str(pisteet), False, black)





run=True    #   set running to true
while run:

    FPS.tick(100)                # FPS clock tick rate 100
    
    # check if the user has closed the display-window or pressed esc
    for event in pygame.event.get():  # all the events in the event queue
        if event.type == pygame.QUIT: # if the player closed the window
            pygame.quit() # the display-window closes
            sys.exit()    # the whole python program exits
        """    
        if event.type == KEYDOWN:     # if the player pressed down any key
            if event.key == K_ESCAPE: # if the key was esc
                pygame.quit() # the display-window closes
                sys.exit()    # the whole python program exits
        """




    # Surface-object which shows the current points
    pisteTeksti = fonttiPisteet.render('Pisteet: '+str(pisteet), False, black)







    # clear the display-surface and draw all the Surfaces again
    windowGame.blit(tausta, (0,0)) # without this, moving characters would have a "trace"
    world.draw()
    drawGrid()
    player.update()
    
    pygame.display.update()
    

import pygame
import config
from pygame.locals import *
from config import *
import random
import math
windowGame =  pygame.display.set_mode((960, 960))
background = pygame.Surface(windowGame.get_size())
background = background.convert()
background.fill((0, 250, 0))

class World():                #   Class to construct our world
    def __init__(self, data):    #   Constructor that takes world data as local variable
        self.tileList = []

        rowCount = 0           #   start at row 0
        for row in data:       #   for loop to iterate through maailma_data and set images accordingly
            columnCount = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(sandImg, (tileSize, tileSize))
                    imgRect = img.get_rect()
                    imgRect.x = columnCount * tileSize        
                    imgRect.y = rowCount * tileSize
                    tile = (img, imgRect)              #   tuple to hold tile image and coordinates
                    self.tileList.append(tile)        #   append tile to tile list
                    
                elif tile == 2:   #   1 = ground
                    img = pygame.transform.scale(grassImg, (tileSize, tileSize))
                    imgRect = img.get_rect()
                    imgRect.x = columnCount * tileSize        
                    imgRect.y = rowCount * tileSize
                    tile = (img, imgRect)              #   tuple to hold tile image and coordinates
                    self.tileList.append(tile)        #   append tile to tile list
                    
                columnCount += 1
            rowCount += 1     #   next row

    def draw(self):
        for tile in self.tileList:        #   iterate through tile list and blit them on screen
            windowGame.blit(tile[0], tile[1])


class Player():                                               #   create Class called Pelaaja
    def __init__(self, x, y, lvl, area, inventory):                                   #   constructor that takes x and y coordinates as local variables
        img = pygame.image.load("img/duck_idle.png").convert_alpha() #   set the picture
        self.bitmap = pygame.transform.scale(img, (31, 31))
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
        if pressedKeys[K_a]:                   #    check key presses for direction of movement
            deltaX -= 3                            #    save where hero would end up but don't move hero yet for collision detecting purposes
        if pressedKeys[K_d]:
            deltaX += 3
        if pressedKeys[K_w]:
            deltaY += -3
        if pressedKeys[K_s]:
            deltaY += 3
        
        
        #   collision testing
        for tile in world.tileList:
            
            #   x collision
            while tile[1].colliderect(self.rect.x + deltaX, self.rect.y, self.playerWidth, self.playerHeight) and deltaX > 0:   #   if we bump into anything simply stop
                deltaX += -1

            while tile[1].colliderect(self.rect.x + deltaX, self.rect.y, self.playerWidth, self.playerHeight) and deltaX < 0:   #   if we bump into anything simply stop
                deltaX += 1

            
            #   y collision
            while tile[1].colliderect(self.rect.x, self.rect.y + deltaY, self.playerWidth, self.playerHeight) and deltaY > 0:
                deltaY += -1                        #   set jump to False after 
                        
            while tile[1].colliderect(self.rect.x, self.rect.y + deltaY, self.playerWidth, self.playerHeight) and deltaY < 0:
                deltaY += 1                        #   set jump to False after touching a surface




        self.rect.x += deltaX        #   deltas have been checked so we add them to the actual coordinates   
        self.rect.y += deltaY
        windowGame.blit(self.bitmap, self.rect)
        

class Enemy():
    def __init__(self, x, y):
        img =  pygame.image.load("img/kivi.png").convert_alpha() 
        self.bitmap = pygame.transform.scale(img (50, 50))
        self.rect = self.bitmap.get_rect()
        self.rect.x = x
        self.rect.y = y


#   create hero pelaaja and the world
player = Player(100, windowHeight - 150, 1, 1, [])
world = World(worldDataGrid)

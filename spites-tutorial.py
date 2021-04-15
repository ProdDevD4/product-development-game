#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 10:57:08 2021

@author: tatti
"""
from __future__ import annotations
import pygame
import sys
from pygame.locals import *
from pathlib import Path
from typing import List
import pyscroll
import pyscroll.data
from pyscroll.group import PyscrollGroup


pygame.init()
clock = pygame.time.Clock()

screen_width = 800
screen_height = 800

# define configuration variables here
CURRENT_DIR = Path(__file__).parent
RESOURCES_DIR = CURRENT_DIR / "data"

# simple wrapper to keep the screen resizeable
def init_screen(width: int, height: int) -> pygame.Surface:
    screen = pygame.display.set_mode((width,height), pygame.RESIZABLE)
    return screen

# make loading images a little easier
def load_image(filename: str) -> pygame.Surface:
    return pygame.image.load(str(RESOURCES_DIR / filename))

class Hero(pygame.sprite.Sprite):
    """Our Hero

    The Hero has three collision rects, one for the whole sprite "rect" and
    "old_rect", and another to check collisions with walls, called "feet".

    The position list is used because pygame rects are inaccurate for
    positioning sprites; because the values they get are 'rounded down'
    as integers, the sprite would move faster moving left or up.

    Feet is 1/2 as wide as the normal rect, and 8 pixels tall.  This size size
    allows the top of the sprite to overlap walls.  The feet rect is used for
    collisions, while the 'rect' rect is used for drawing.

    There is also an old_rect that is used to reposition the sprite if it
    collides with level walls.
    """

    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.image = load_image("hero.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 8)
        self.inventory = []
        self.rect.center = [pos_x,pos_y]


screen = init_screen(800, 800)
hero = Hero(200,100)
hero_group = pygame.sprite.Group()
hero_group.add(hero)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.flip()
    hero_group.draw(screen)
    clock.tick(60)
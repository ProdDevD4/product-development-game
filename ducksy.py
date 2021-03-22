""" 
D4 GÄNG presents:
                                                         
▀███▀▀▀██▄                   ▀███                        
  ██    ▀██▄                   ██                        
  ██     ▀█████  ▀███  ▄██▀██  ██  ▄██▀ ▄██▀█████▀   ▀██▀
  ██      ██ ██    ██ ██▀  ██  ██ ▄█    ██   ▀▀ ██   ▄█  
  ██     ▄██ ██    ██ ██       ██▄██    ▀█████▄  ██ ▄█   
  ██    ▄██▀ ██    ██ ██▄    ▄ ██ ▀██▄  █▄   ██   ███    
▄████████▀   ▀████▀███▄█████▀▄████▄ ██▄▄██████▀   ▄█     
                                                ▄█       
                                              ██▀        
                                                                 ▄▄▄▄                       
▀████▄     ▄███▀      ▀███▀▀▀██▄                   ▀███        ▄█▀ ▀▀                       
  ████    ████          ██    ▀██▄                   ██        ██▀                          
  █ ██   ▄█ ██  ▄██▀██  ██     ▀█████  ▀███  ▄██▀██  ██  ▄██▀ █████  ▄█▀██▄  ▄██▀██  ▄▄█▀██ 
  █  ██  █▀ ██ ██▀  ██  ██      ██ ██    ██ ██▀  ██  ██ ▄█     ██   ██   ██ ██▀  ██ ▄█▀   ██
  █  ██▄█▀  ██ ██       ██     ▄██ ██    ██ ██       ██▄██     ██    ▄█████ ██      ██▀▀▀▀▀▀
  █  ▀██▀   ██ ██▄    ▄ ██    ▄██▀ ██    ██ ██▄    ▄ ██ ▀██▄   ██   ██   ██ ██▄    ▄██▄    ▄
▄███▄ ▀▀  ▄████▄█████▀▄████████▀   ▀████▀███▄█████▀▄████▄ ██▄▄████▄ ▀████▀██▄█████▀  ▀█████▀
                                                                                            
                                                                                            
                           ▄▄                                                     
  ▄▄█▀▀▀█▄█              ▀███                                                     
▄██▀     ▀█                ██                                                ▄▄▄  
██▀       ▀ ▄██▀██▄   ▄█▀▀███   ▄▄█▀██ ▄██▀███     ▄█▄▀▄█▄▄▄██▀▀██▄ ▄██▀▀██▄▀███  
██         ██▀   ▀██▄██    ██  ▄█▀   ████   ▀▀    ███    ███▀    ▀███▀    ▀██ ██  
██▄        ██     █████    ██  ██▀▀▀▀▀▀▀█████▄    ███    ███      ███      ██ ██  
▀██▄     ▄▀██▄   ▄██▀██    ██  ██▄    ▄█▄   ██     ▀████████▄    ▄███▄    ▄██ ██  
  ▀▀█████▀  ▀█████▀  ▀████▀███▄ ▀█████▀██████▀          ▄█▀▀██████▀ ▀██████▀▄████▄
                                                     ▄██                          
                                                   █▀▀                            

Verion 0.9.1 ALPHA

"""
from __future__ import annotations

from pathlib import Path
from typing import List

import pygame
import config
import classes
from pygame.locals import *
from config import *
from classes import *
import random
import sys     # sys-module will be needed to exit the program
import pytmx
from pytmx.util_pygame import load_pygame

import pyscroll
import pyscroll.data
from pyscroll.group import PyscrollGroup




# simple wrapper to keep the screen resizeable
def init_screen(width: int, height: int) -> pygame.Surface:
    screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
    return screen


# make loading images a little easier
def load_image(filename: str) -> pygame.Surface:
    return load_image(str(RESOURCES_DIR / filename))


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

    def __init__(self) -> None:
        super().__init__()
        """
        self.walk = []
        self.walk.append(pygame.image.load("data/walk1.png").convert_alpha())
        self.walk.append(pygame.image.load("data/walk2.png").convert_alpha())
        
        self.up = []
        self.up.append(pygame.image.load("data/up1.png").convert_alpha())
        self.up.append(pygame.image.load("data/up2.png").convert_alpha())
        
        self.walk_index = 0
        self.up_index = 0
        
        self.walk_image = self.walk[self.walk_index]
        self.up_image = self.up[self.up_index]
        """
        self.images = []
        self.images.append(pygame.image.load("data/walk1.png").convert_alpha())
        self.images.append(pygame.image.load("data/hero.png").convert_alpha())
        self.images.append(pygame.image.load("data/walk2.png").convert_alpha())
        
        self.index = 0
        
        self.image = self.images[self.index]
        self.image = pygame.image.load("data/hero.png").convert_alpha()
        self.velocity = [0, 0]
        self._position = [0.0, 0.0]
        self._old_position = self.position
        self.rect = self.image.get_rect()
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 8)

    @property
    def position(self) -> List[float]:
        return list(self._position)

    @position.setter
    def position(self, value: List[float]) -> None:
        self._position = list(value)

    def update(self, dt: float) -> None:

        
        self._old_position = self._position[:]
        self._position[0] += self.velocity[0] * dt
        self._position[1] += self.velocity[1] * dt
        self.rect.topleft = self._position
        self.feet.midbottom = self.rect.midbottom
        
        """self.walk_index += 1
        self.up_index += 1
        if self.walk_index >= len(self.walk):
            self.walk_index = 0
        if self.up_index >= len(self.up):
            self.up_index = 0
        self.walk_image = self.walk[self.walk_index]
        self.up_image = self.up[self.up_index]"""
        #when the update method is called, we will increment the index
        self.index += 1
 
        #if the index is larger than the total images
        if self.index >= len(self.images):
            #we will make the index to 0 again
            self.index = 0
        
        #finally we will update the image that will be displayed
        self.image = self.images[self.index]

    def move_back(self, dt: float) -> None:
        """If called after an update, the sprite can move back"""
        self._position = self._old_position
        self.rect.topleft = self._position
        self.feet.midbottom = self.rect.midbottom


class DucksyGame:
    """This class is a basic game.

    This class will load data, create a pyscroll group, a hero object.
    It also reads input and moves the Hero around the map.
    Finally, it uses a pyscroll group to render the map and Hero.
    """

    map_path = RESOURCES_DIR / "level0.tmx"

    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen

        # true while running
        self.running = False

        # load data from pytmx
        tmx_data = load_pygame(self.map_path)

        # setup level geometry with simple pygame rects, loaded from pytmx
        self.walls = []
        for obj in tmx_data.objects:
            self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # create new data source for pyscroll
        map_data = pyscroll.data.TiledMapData(tmx_data)

        # create new renderer (camera)
        self.map_layer = pyscroll.BufferedRenderer(
            map_data, screen.get_size(), clamp_camera=False, tall_sprites=1
        )
        self.map_layer.zoom = 2

        # pyscroll supports layered rendering.  our map has 3 'under' layers
        # layers begin with 0, so the layers are 0, 1, and 2.
        # since we want the sprite to be on top of layer 1, we set the default
        # layer for sprites as 2
        self.group = PyscrollGroup(map_layer=self.map_layer, default_layer=2)

        self.hero = Hero()

        # put the hero in the center of the map
        self.hero.position = self.map_layer.map_rect.center
        self.hero._position[0] += 200
        self.hero._position[1] += 400

        # add our hero to the group
        self.group.add(self.hero)

    def draw(self) -> None:

        # center the map/screen on our Hero
        self.group.center(self.hero.rect.center)

        # draw the map and all sprites
        self.group.draw(self.screen)

    def handle_input(self) -> None:
        """Handle pygame input events"""
        poll = pygame.event.poll

        event = poll()
        while event:
            if event.type == QUIT:
                self.running = False
                break

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = False
                    break

                elif event.key == K_EQUALS:
                    self.map_layer.zoom += 0.25

                elif event.key == K_MINUS:
                    value = self.map_layer.zoom - 0.25
                    if value > 0:
                        self.map_layer.zoom = value

            # this will be handled if the window is resized
            elif event.type == VIDEORESIZE:
                self.screen = init_screen(event.w, event.h)
                self.map_layer.set_size((event.w, event.h))

            event = poll()

        # using get_pressed is slightly less accurate than testing for events
        # but is much easier to use.
        pressed = pygame.key.get_pressed()
        if pressed[K_UP]:
            self.hero.velocity[1] = -HERO_MOVE_SPEED
        elif pressed[K_DOWN]:
            self.hero.velocity[1] = HERO_MOVE_SPEED

        elif pressed[K_w]:
            self.hero.velocity[1] = -HERO_MOVE_SPEED
        elif pressed[K_s]:
            self.hero.velocity[1] = HERO_MOVE_SPEED
        else:
            self.hero.velocity[1] = 0

        if pressed[K_LEFT]:
            self.hero.velocity[0] = -HERO_MOVE_SPEED
        elif pressed[K_RIGHT]:
            self.hero.velocity[0] = HERO_MOVE_SPEED

        elif pressed[K_a]:
            self.hero.velocity[0] = -HERO_MOVE_SPEED
        elif pressed[K_d]:
            self.hero.velocity[0] = HERO_MOVE_SPEED
        else:
            self.hero.velocity[0] = 0


    def update(self, dt):
        """Tasks that occur over time should be handled here"""
        self.group.update(dt)

        # check if the sprite's feet are colliding with wall
        # sprite must have a rect called feet, and move_back method,
        # otherwise this will fail
        for sprite in self.group.sprites():
            if sprite.feet.collidelist(self.walls) > -1:
                sprite.move_back(dt)

    def run(self):
        """Run the game loop"""
        clock = pygame.time.Clock()
        self.running = True

        from collections import deque

        times = deque(maxlen=30)

        try:
            while self.running:
                dt = clock.tick() / 1000.0
                times.append(clock.get_fps())

                self.handle_input()
                self.update(dt)
                self.draw()
                pygame.display.flip()

        except KeyboardInterrupt:
            self.running = False


def main() -> None:
    pygame.init()
    pygame.font.init()
    screen = init_screen(800, 600)
    pygame.display.set_caption("Ducksy McDucface Codes 9001")

    try:
        game = DucksyGame(screen)
        game.run()
    except KeyboardInterrupt:
        pass
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()

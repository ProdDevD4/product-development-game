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

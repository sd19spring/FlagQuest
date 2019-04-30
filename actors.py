import pygame

def make_image(color, size):
    """Makes a rectangular image.

    color: Tuple of the RGB color code
    size: Tuple of the size of the image in pixels

    returns: image"""
    image = pygame.Surface(size)
    image.fill(color)
    return image

def cell_to_pixel():
    """Converts cell coordinates to pixel coordinates"""
    # this could be used for drawing stuff
    pass

class Actor():
    """
    The Actor class contains generic information which can be inherinted by all actors.
    """
    def __init__(self, image, size, position):
        """Initialize the actor.

        image: image file of the actor
        size: Tuple of the size of the actor in pixels
        position: Tuple of the position of the actor in pixels
        """
        # pygame.sprite.Sprite.__init__(self) # set up the actor's spriteness
        self.image = image
        self.size = size
        self.position = position
        self.rect = self.image.get_rect(topleft = self.position)

class Color(Actor):
    """
    The Color_Actor class contains the state and sprite
    of each color of the flag.
    """
    def __init__(self, color, size, position):
        """Initialize the Color_Actor object

        color: Tuple of the RGB color code
        size: Tuple of the size in pixels
        position: Tuple of the position in pixels
        """
        image = make_image(color, size)
        super(Color, self).__init__(image, size, position)

        self.exists = True      # used in make_model to make actor disappear if collided with
        self.color = color
        # CAN WE REMOVE THE COLOR ONCE IT IS PICKED UP?

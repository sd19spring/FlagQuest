import pygame

class Actor():
    """
    The Actor class contains generic information which can be inherinted by all actors.
    """
    def __init__():
        pass

    def cell_to_pixel():
        """Converts cell coordinates to pixel coordinates"""
        # this could be used for drawing stuff
        pass

class Color(pygame.sprite.Sprite):
    """
    The Color_Actor class contains the state and sprite
    of each color of the flag.
    """
    def __init__(self, color, model, position):
        """Initialize the Color_Actor object

        color: Tuple of the RGB color code
        model: Model object for the world
        position: cell coordinates of the color
        """
        pygame.sprite.Sprite.__init__(self) # set up the actor's spriteness
        self.position = position
        self.size = (model.cell_size)
        self.make_image(color)
        self.rect = self.image.get_rect(topleft = self.position)

        self.exists = True      # used in make_model to make actor disappear if collided with
        self.color = color
        # CAN WE REMOVE THE COLOR ONCE IT IS PICKED UP?

    def make_image(self, color):
        """Makes the image for the flag stripe from a given color"""
        self.image = pygame.Surface(self.size)
        self.image.fill(color)

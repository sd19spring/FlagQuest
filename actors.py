import pygame

class Actor():
    """
    The Actor class contains generic information which can be inherinted by all actors.
    """
    def __init__():
        pass

class Color(pygame.sprite.Sprite):
    """
    The Color_Actor class contains the state and sprite
    of each color of the flag.
    """
    def __init__(self, color, model, position):
        """Initialize the Color_Actor object

        color: Tuple of the RGB color code
        model:
        """
        pygame.sprite.Sprite.__init__(self) # set up the actor's spriteness
        print(color)
        self.color = color
        self.position = position
        self.rect = pygame.Rect(self.position[0], self.position[1], model.cell_size, model.cell_size)
        self.exists = True      # used in make_model to make actor disappear if collided with

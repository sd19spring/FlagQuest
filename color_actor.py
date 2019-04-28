"""
The Color_Actor class contains the state and sprite
of each color in the game map. Right now, instead of a
sprite it appears as a colored grid cell
"""
import pygame

class Color_Actor(pygame.sprite.Sprite):
    def __init__(self, color, model, x=0, y=0):
        pygame.sprite.Sprite.__init__(self) # set up the actor's spriteness

        self.color = color
        self.x = x
        self.y = y
        self.position = (self.x, self.y)
        self.rect = pygame.Rect(x, y, model.cell_size, model.cell_size)
        self.exists = True      # used in make_model to make actor disappear if collided with

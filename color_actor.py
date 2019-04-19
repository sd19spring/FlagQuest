"""
The Color_Actor class contains the state and sprite
of each color in the game map. Right now, instead of a
sprite it appears as a colored grid cell
"""
import pygame

class Color_Actor(pygame.sprite.Sprite):
    def __init__(self, color, model, x=0, y=0):
        self.color = color
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, model.cell_size, model.cell_size)

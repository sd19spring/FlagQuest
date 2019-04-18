import pygame

class Color_Actor(pygame.sprite.Sprite):
    def __init__(self, color, x=0, y=0):
        self.color = color
        self.x = x
        self.y = y

import pygame

class Color_Actor(pygame.sprite.Sprite):
    def __init__(self, color, model, x=0, y=0):
        self.color = color
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, model.cell_size, model.cell_size)

    # def update_rect(self, model):
    #     self.rect = pygame.Rect(self.x, self.y, model.cell_size, model.cell_size)

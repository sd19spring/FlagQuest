import pygame
import player_actor

class Game_Window(object):
    def __init__(self, model, x_size, y_size):
        self.model = model
        self.x_size = x_size
        self.y_size = y_size
        self.screen = pygame

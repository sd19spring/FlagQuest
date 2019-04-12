import pygame
import time
from player_actor import *
from controller import *

class View():
    def __init__(self, width, height, filling):
        self.screen = pygame.display.set_mode((width, height))  # sets screen dimensions
        self.screen.fill(filling)        # sets background color
        pygame.display.set_caption('Window Viewer')             # sets window caption
        pygame.display.flip()            # updates contents of entire display


window = pygame.display.set_mode((640, 400))
window.fill((144, 238, 144))    # a painfully bright tone of green

BLUE = (0, 0, 255)
buddy = Player_actor(10,20,90,BLUE,width = 50, height = 70)

def update():
    buddy.get_keypress()
    buddy.move()
    buddy.draw(window)
    time.sleep(.01)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    update()

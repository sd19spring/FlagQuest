import pygame
import time
import gameworld
from pygame.locals import *
from controller import *
from flag import Flag
from level_generation import *

class Game():
    """Class to manage the actor and gameworld classes"""
    def __init__(self, size=(1880,1080), fill=(0, 0, 0)):
        """Create the world.

        size: Tuple of the window dimensions
        fill: Tuple of the RGB color"""
        # add file image?
        self.fill_color = fill
        self.model = gameworld.Model()
        self.view = view = gameworld.View(size, self.fill_color, self.model)
        self.running = True

    def check_events(self):
        """Check the events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            # add function to check for movement
            elif event.type == KEYDOWN and self.model.endgame == True:
                self.model.endscreen.pressed(event.key)
            if event.type == KEYDOWN and event.key == pygame.K_ESCAPE: # if escape is pressed
                pygame.display.set_mode((1880, 1080), pygame.RESIZABLE)

    def check_collision(self):
        # touched_piece is a piece of the flag that the player just collided with (if they even did)
        touched_piece = self.model.player.check_color_collision(self.model.color_objs)
        if touched_piece:
            touched_piece.exists = False          # makes the touched piece disappear
            self.model.flag.add_color(touched_piece)     # add stripe to the flag graphic
            if self.model.flag.complete() == True:
                self.model.make_endscreen()
                self.model.endgame = True
                self.fill_color=(255, 255, 255)

    def update(self):
        """Updates the game for one tick"""
        self.check_events()
        self.check_collision()
        self.view.update()
        time.sleep(0.01)

def play_game():

    game = Game()

    while game.running:
        game.update()

if __name__ == '__main__':

    play_game() # start running game

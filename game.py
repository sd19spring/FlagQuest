import pygame
import time
import gameworld
from pygame.locals import *
from player_actor import *
from controller import *
from obstacles import *
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
            elif event.type == KEYDOWN and self.model.endgame == True:
                self.model.endscreen.pressed(event.key)

    def check_movement():
        pass

    def check_collision(self):
        # touched_piece is a piece of the flag that the player just collided with (if they even did)
        touched_piece = self.model.player.check_color_collision(self.model.color_objs)
        if touched_piece:
            touched_piece.exists = False          # makes the touched piece disappear
            self.model.flag.add_color(touched_piece)     # add stripe to the flag graphic
            if self.model.flag.complete() == True:
                self.model.make_endscreen()
                self.view.endgame = True
                self.fill_color=(255, 255, 255)

    def endgame():
        pass

def play_game():
    # pygame.init() # necessary?

    # model = gameworld.Model()
    # fill_color = (0, 0, 0)
    # view = gameworld.View(size, fill_color, model)

    #######TESTS
    # print(get_valid_path(game.model, game.model.grid_cells[(3,3)], game.model.grid_cells[(20,20)]))
    game = Game()
    while game.running:
        game.check_events()
        game.check_collision()
        game.view.update()
        time.sleep(0.01)

if __name__ == '__main__':

    play_game() # start running game

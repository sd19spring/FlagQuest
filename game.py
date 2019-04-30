import pygame
import time
import gameworld
from pygame.locals import *
from player_actor import *
from controller import *
from obstacles import *
from flag import Flag
from level_generation import *
# class Game():
#     """
#     Game model to create the world and check events
#     """
#     def check_events():
#         pass
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

    def check_events():
        """Check the events"""
        pass

    def check_movement():
        pass

    def check_collision():
        pass

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
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == KEYDOWN and game.view.endgame == True:
                game.model.endscreen.pressed(event.key)
        touched_piece = game.model.player.check_color_collision(game.model.color_objs)    # touched_piece is a piece of the flag that the player just collided with (if they even did)
        if touched_piece:
            touched_piece.exists = False          # makes the touched piece disappear
            game.model.flag.add_color(touched_piece)     # add stripe to the flag graphic
            if game.model.flag.complete() == True:
                game.model.make_endscreen()
                game.view.endgame = True
                game.fill_color=(255, 255, 255)
        game.view.screen.fill(game.fill_color)           # cleans up the screen at each runthrough
        game.view.update()         # updates the model based on any new inputs or in-game events
        time.sleep(0.01)

if __name__ == '__main__':

    play_game() # start running game

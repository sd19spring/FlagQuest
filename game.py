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

def play_game(size):
    pygame.init()

    model = gameworld.Model()
    fill_color = (0, 0, 0)
    view = gameworld.View(size, fill_color, model)

    #######TESTS
    print(get_valid_path(model, model.grid_cells[(3,3)], model.grid_cells[(20,20)]))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == KEYDOWN and view.endgame == True:
                model.endscreen.pressed(event.key)
        touched_piece = model.player.check_color_collision(model.color_objs)    # touched_piece is a piece of the flag that the player just collided with (if they even did)
        if touched_piece:
            touched_piece.exists = False          # makes the touched piece disappear
            model.flag.add_color(touched_piece)     # add stripe to the flag graphic
            if model.flag.complete() == True:
                model.make_endscreen()
                view.endgame = True
                fill_color=(255, 255, 255)
        view.screen.fill(fill_color)           # cleans up the screen at each runthrough
        view.update()         # updates the model based on any new inputs or in-game events
        time.sleep(0.01)

if __name__ == '__main__':

    play_game((1880,1080)) # start running game

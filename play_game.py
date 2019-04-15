import pygame
import time
from player_actor import *
from controller import *
from make_model import Model
from obstacles import *

class View():
    def __init__(self, width, height, filling, model):
        self.model = model
        self.screen = pygame.display.set_mode((width, height))  # sets screen dimensions
        self.screen.fill(filling)        # sets background color
        pygame.display.set_caption('Window Viewer')             # sets window caption

    def draw_player(self, player_actor):
        player_actor.draw(self.screen)

    def draw_color_actors(self):
        for i in range(len(self.model.color_objs)):
            pygame.draw.circle(self.screen,
                               pygame.Color(self.model.colors[i][0], self.model.colors[i][1], self.model.colors[i][2]),
                               [self.model.color_objs[i].x,
                               self.model.color_objs[i].y],
                               10)

    def draw_obstacles(self):
        for obstacle in self.model.obstacles:
            obstacle.draw(self.screen)

    def update(self, player_actor):
        self.draw_player(player_actor)
        self.draw_color_actors()
        self.draw_obstacles()
        pygame.display.update()

def play_game(size):
    pygame.init()

    model = Model()
    view = View(size[0], size[1], (0, 0, 0), model)
    BLUE = (0, 0, 255)
    player = Player_actor(10,20,90,BLUE,width = 50, height = 70)
    view.model.make_obstacles()     # this is here because we don't want to make new obstacles at each event loop

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        view.screen.fill((0,0,0))           # cleans up the screen at each runthrough
        view.update(player)         # updates the model based on any new inputs or in-game events
        # print(player)     # this is just to show details of the player's movement
        time.sleep(0.01)

if __name__ == '__main__':

    size = (640,400)
    play_game(size) # start running game

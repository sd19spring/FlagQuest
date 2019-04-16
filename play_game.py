import pygame
from pygame.locals import *
import time
from player_actor import *
from controller import *
from make_model import Model
from obstacles import *
from flag_class import Flag

class View():
    def __init__(self, width, height, filling, model):
        self.model = model
        self.screen = pygame.display.set_mode((width, height))  # sets screen dimensions
        self.screen.fill(filling)        # sets background color
        pygame.display.set_caption('Window Viewer')             # sets window caption

    def draw_player(self, player_actor):
        """Blits the screen with the player_actor at its position (i.e. x_pos,y_pos)"""
        player_actor.update_image()
        self.screen.blit(player_actor.image, player_actor.position)   # places image of player_actor

    def draw_color_actors(self):
        for i in range(len(self.model.color_objs)):
            pygame.draw.rect(self.screen,
                             pygame.Color(self.model.flag.colors[i][0],
                             self.model.flag.colors[i][1], self.model.flag.colors[i][2]),
                             pygame.Rect(self.model.color_objs[i].x, self.model.color_objs[i].y, self.model.cell_size, self.model.cell_size))


    def draw_obstacles(self):
        for obstacle in self.model.obstacles:
            self.screen.blit(obstacle.image, obstacle.position)

    def draw_grid(self):
        for i in range(self.model.grid_size):
            for j in range(self.model.grid_size):
                    pygame.draw.circle(self.screen,
                                       pygame.Color(255, 255, 255),
                                       [self.model.grid_cells[(i, j)].cell_coord[0], self.model.grid_cells[(i, j)].cell_coord[1]],
                                       5)


    def update(self, player_actor):
        self.draw_player(player_actor)
        self.draw_color_actors()
        self.draw_obstacles()
        self.draw_grid()
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
            #flag test - to be integrated
            if event.type == KEYDOWN and event.key == K_SPACE:
                view.model.flag.num_colors_up += 1

        view.screen.fill((0,0,0))           # cleans up the screen at each runthrough
        view.update(player)         # updates the model based on any new inputs or in-game events
        # print(player)     # this is just to show details of the player's movement

        #does not yet work, indicating images are loading incorrectly
        view.model.flag.draw(view.screen) #flag test - to be integrated

        time.sleep(0.01)

if __name__ == '__main__':

    size = (800,800)
    play_game(size) # start running game

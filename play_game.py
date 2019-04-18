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

    def draw_player(self):
        """Blits the screen with the player_actor at its position (i.e. x_pos,y_pos)"""
        player = self.model.player
        player.update_position()
        self.screen.blit(player.image, player.draw_position)   # places image of player_actor

    def draw_color_actors(self):
        for i in range(len(self.model.color_objs)):
            pygame.draw.rect(self.screen,
                             pygame.Color(self.model.flag.colors[i][0],
                             self.model.flag.colors[i][1], self.model.flag.colors[i][2]),
                             pygame.Rect(self.model.color_objs[i].x, self.model.color_objs[i].y, self.model.cell_size, self.model.cell_size))


    def draw_obstacles(self):
        for obstacle in self.model.obstacles:       # places image of obstacle for each obstacle created in Model
            self.screen.blit(obstacle.image, obstacle.position)

    def draw_grid(self):
        for i in range(self.model.grid_size):
            for j in range(self.model.grid_size):
                    pygame.draw.circle(self.screen,
                                       pygame.Color(255, 255, 255),
                                       [self.model.grid_cells[(i, j)].cell_coord[0], self.model.grid_cells[(i, j)].cell_coord[1]],
                                       5)

    def draw_flag(self):
        if self.model.flag.num_colors_up:
            for i in list(range(self.model.flag.num_colors_up)):
                self.screen.blit(self.model.flag.image_pieces[i], self.model.flag.position)

    def update(self):
        self.draw_player()
        self.draw_color_actors()
        self.draw_obstacles()
        self.draw_grid()
        self.draw_flag()
        pygame.display.update()

def play_game(size):
    pygame.init()

    model = Model()
    view = View(size[0], size[1], (0, 0, 0), model)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            #flag test - to be integrated
            if event.type == KEYDOWN and event.key == K_SPACE:
                view.model.flag.num_colors_up += 1


        view.screen.fill((0,0,0))           # cleans up the screen at each runthrough
        view.update()         # updates the model based on any new inputs or in-game events

        time.sleep(0.01)

if __name__ == '__main__':

    size = (800,800)
    play_game(size) # start running game

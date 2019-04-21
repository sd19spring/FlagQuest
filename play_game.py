import pygame
from pygame.locals import *
import time
from player_actor import *
from controller import *
from make_model import Model
from obstacles import *
from flag import Flag

class View():
    """
    Instantiates model and draws the state of every object on the game screen
    """
    def __init__(self, screen_size, filling, model):
        """ Initialize model and make game screen """
        self.model = model
        self.screen = pygame.display.set_mode(screen_size)  # sets screen dimensions
        self.screen.fill(filling)        # sets background color
        pygame.display.set_caption('Window Viewer')             # sets window caption

    def draw_player(self):
        """Blits the screen with the player_actor at its position (i.e. x_pos,y_pos)"""
        self.model.player.update_position()
        self.screen.blit(self.model.player.image, self.model.player.get_draw_position())   # places image of player_actor

    def draw_color_actors(self):
        """Draw the flag colors onto the display"""
        for i in range(len(self.model.color_objs)):
            pygame.draw.rect(self.screen,
                             pygame.Color(self.model.flag.colors[i][0],
                             self.model.flag.colors[i][1], self.model.flag.colors[i][2]),
                             pygame.Rect(self.model.color_objs[i].x, self.model.color_objs[i].y, self.model.cell_size, self.model.cell_size))


    def draw_obstacles(self):
        """Draw the obstacles on the display"""
        for obstacle in self.model.obstacles:       # places image of obstacle for each obstacle created in Model
            self.screen.blit(obstacle.image, obstacle.position)

    def draw_grid(self):
        """Draw the grid on the display"""
        for i in range(self.model.grid_x_size):
            for j in range(self.model.grid_y_size):
                    pygame.draw.circle(self.screen,
                                       pygame.Color(255, 255, 255),
                                       [self.model.grid_cells[(i, j)].cell_coord[0], self.model.grid_cells[(i, j)].cell_coord[1]],
                                       5)

    def draw_flag(self):
        """Draw the flag onto the display"""
        if self.model.flag.num_colors_up:
            for i in list(range(self.model.flag.num_colors_up)):
                self.screen.blit(self.model.flag.image_pieces[i], self.model.flag.position)

    def draw_darkness(self):
        """Draw the darkness on the display"""
        self.model.darkness.rotate()
        self.screen.blit(self.model.darkness.image, self.model.darkness.draw_position())   # places image of player_actor

    def update(self):
        """Update the draw positons of player, color_actors, obstacles, grid, and the flag"""
        self.draw_player()
        self.draw_color_actors()
        self.draw_obstacles()
        self.draw_grid()
        self.draw_flag()
        self.draw_darkness()
        pygame.display.update()

def play_game(size):
    pygame.init()

    model = Model()
    view = View(size, (0, 0, 0), model)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        color_collision = model.player.check_color_collision(model)
        if color_collision:
            model.flag.add_color()


        view.screen.fill((0,0,0))           # cleans up the screen at each runthrough
        view.update()         # updates the model based on any new inputs or in-game events

        time.sleep(0.01)

if __name__ == '__main__':

    play_game((1200,800)) # start running game

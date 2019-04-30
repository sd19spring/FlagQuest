import pygame
import random
import actors
from flag import Flag
from obstacles import *
from darkness import *
from education_screen import *

# def random_coord(min_coord, max_coord):
#     """Find a random coordinate.
#
#     draw_area: Tuple of the eligible screen area to draw in
#
#     returns: Tuple"""
#     x_cell = random.randint(min_coord[0], max_coord[0])
#     y_cell = random.randint(min_coord[1], max_coord[1])
#     return (x_cell, y_cell)

def pixels(coord):
    """Get the pixel coordinates of a cell_coordinates.

    coord: Tuple of the cell coordinates

    returns: Tuple of the pixel coordinates"""


class Cell(object):
    """ This is an object for each grid cell """
    def __init__(self, cell_coord, grid_coord, occupied, type, label):
        self.cell_coord = cell_coord # coordinates of upper left corner of cell in pixels, tuple
        self.grid_coord = grid_coord # coordinates of cell in terms of position in grid, tuple
        self.occupied = occupied
        self.type = type
        self.label = label

class Model(object):
    """ Class that holds the state of the entire game """
    def __init__(self, cell_size = (40, 40), grid_size = (46, 23)):
        """
        Initialize the model.

        cell_size: Tuple of the dimension of each cell in pixels
        grid_size: Tuple of the dimensions of the grid in cells"""

        self.cell_size = cell_size
        self.grid_size = grid_size
        self.endgame = False
        self.make_grid()
        self.choose_flag()
        self.make_colors()
        self.make_obstacles()
        self.make_player()
        self.make_darkness()

    def make_grid(self):
        """Instantiate grid cells for game map.

        Creates a dictionary with keys that are cell
        coordinates with values that are cell objects"""
        self.grid_cells = {}
        cell_size = (self.cell_size) # cell size in pixels
        for i in range(self.grid_size[0]): # for the x cells
            for j in range(self.grid_size[1]): # for the y cells
                cell_coord = (i*self.cell_size[0], 160+j*self.cell_size[1])
                self.grid_cells[(i,j)] = Cell(cell_coord, (i, j), False, 'none', (i,j))

    def choose_flag(self):
        """Randomly choose which flag to play the game with."""
        # TO DO
        name = 'trans'
        self.flag = Flag(name)
        print("You are playing with the " + self.flag.name + " flag")

    def make_colors(self):
        """Instantiate Color objects for each color in the chosen flag."""
        self.color_objs = []
        for color in self.flag.colors:
            # could we have a get random coord method?
            x_cell = random.randint(0, self.grid_size[0]-1)
            y_cell = random.randint(0, self.grid_size[1]-1)
            # coord = self.grid_cells[random_coord]
            # coord = random_coord((0, 0), (self.grid_size))
            coord = self.grid_cells[(x_cell,y_cell)].cell_coord
            # coord = (x_cell, y_cell)
            self.color_objs.append(actors.Color(color, self.cell_size, coord))
            self.grid_cells[(x_cell,y_cell)].occupied = True
            self.grid_cells[(x_cell,y_cell)].type = 'color'


    def make_obstacles(self):
        """Generate obstacles in the grid"""
        self.obstacles = []              # instantiates a list of all obstacle sprite groups
        self.cleared_obstacles = []

        obstacle_types = self.flag.colors      # makes list of possible obstacle types based off of the flag's colors

        for i in range(200):     # 10 is arbitrary, we should replace with intentional number later
            x_cell = random.randint(0, self.grid_size[0]-1)        # randomizes location of obstacle
            y_cell = random.randint(0, self.grid_size[1]-1)
            while self.grid_cells[(x_cell, y_cell)].occupied == True:   # re-randomizes location if the location is occupied by a color_obj
                x_cell = random.randint(0, self.grid_size[0]-1)
                y_cell = random.randint(0, self.grid_size[1]-1)

            coord = self.grid_cells[(x_cell,y_cell)].cell_coord
            type = random.choice(obstacle_types)            # randomly chooses this obstacle's type
            obstacle = Obstacle((self.cell_size),coord,type)

            obstacle.make_groups(obstacle, type, self.obstacles)    # add obstacle to group based on what the obstacle's type is

            self.grid_cells[(x_cell,y_cell)].occupied = True
            self.grid_cells[(x_cell,y_cell)].type = 'obstacle'

    def erase_obstacles(self, key = pygame.K_SPACE):
        """
        while spacebar is held, all obstacles corresponding to all collided_with colors are removed from self.model.obstacles, therefor erased from screen
        if/when spacebar is released, all obstacles are added back to self.model.obstacles and reappear on the screen

        erased obstacles do not block movement; it is as if the obstacles don't exist. once they re-appear, they act like normal obstacles again

        this method erases obstacles corresponding with ALL colors in self.model.player.collided_with
        """
        if pygame.key.get_pressed()[key] == 1:
            for color in self.player.collided_with:   # iterates through list of colors that have been collided with
                for group in self.obstacles:        # iterates through all groups of obstacles
                    if group.type == color.color:      # finds group that corresponds to color that was just touched
                        self.obstacles.remove(group)
                        self.cleared_obstacles.append(group)
        else:
            for group in self.cleared_obstacles:
                self.cleared_obstacles.remove(group)
                self.obstacles.append(group)

    def make_player(self):
        """ Instantiate Player object """
        coord = (self.cell_size[0]*self.grid_size[0], self.cell_size[1]*self.grid_size[1]+160)
        self.player = actors.Player((400, 400), coord, self.obstacles, self.color_objs)
        # should just pass WORLD

    def make_darkness(self):
        """ Instantiate Darkness object"""
        self.darkness = Darkness(self.player, (self.cell_size[0]*self.grid_size[0], self.cell_size[1]*self.grid_size[0]))

    def make_endscreen(self):
        """ Instantiate Endscreen object"""
        self.endscreen = EndScreen(self.flag.name, (1920, 1080))

class View():
    """
    Instantiates model and draws the state of every object on the game screen
    """
    def __init__(self, screen_size, filling, model):
        """ Initialize model and make game screen """
        self.model = model
        self.screen = pygame.display.set_mode(screen_size, pygame.FULLSCREEN)  # sets screen dimensions
        self.fill_color = filling
        self.screen.fill(self.fill_color)        # sets background color
        pygame.display.set_caption('Window Viewer')             # sets window caption

    def draw_player(self):
        """Blits the screen with the player_actor at its position (i.e. x_pos,y_pos)"""
        self.model.player.update_position()
        # position = get draw position
        self.screen.blit(self.model.player.image, self.model.player.get_draw_position())   # places image of player_actor
        # print(self.model.player.grid_cell)

    def draw_colors(self):
        """Draw the flag colors onto the display"""
        for piece in self.model.color_objs:
            if piece.exists:
                self.screen.blit(piece.image, piece.position)

    def draw_obstacles(self):
        """Draw the obstacles on the display"""
        for group in self.model.obstacles:       # places image of obstacle for each obstacle created in Model
            group.draw(self.screen)
        self.model.erase_obstacles()        # runs method that allows player to erase colored obstacles by holding spacebar. change key argument to change the trigger key

    def draw_grid(self):
        """Draw the grid on the display"""
        for i in range(self.model.grid_size[0]):
            for j in range(self.model.grid_size[1]):
                    pygame.draw.circle(self.screen,
                                       pygame.Color(255, 255, 255),
                                       [self.model.grid_cells[(i, j)].cell_coord[0], self.model.grid_cells[(i, j)].cell_coord[1]],
                                       5)

    def draw_flag(self):
        """Draw the flag onto the display"""
        if self.model.flag.colors_up:
            for image in self.model.flag.colors_up:
                self.screen.blit(image, self.model.flag.position)

    def draw_darkness(self):
        """Draw the darkness on the display"""
        self.model.darkness.rotate()
        self.screen.blit(self.model.darkness.image, self.model.darkness.draw_position())   # places image of player_actor

    def draw_endscreen(self):
        """Draw the endscreen on the display"""
        # draw the current page in the book
        self.screen.blit(self.model.endscreen.book.pages[self.model.endscreen.book.current_page].image, (0, 0))

    def draw_background(self):
        # plan to add the fill section here
        pass

    def update(self):
        """Update the draw positons of player, color_actors, obstacles, grid, and the flag"""
        self.screen.fill(self.fill_color) # can you fill with an image?
        if self.model.endgame == False:
            # self.draw() ??
                # for actor in actors:
                    # draw
            # self.update_pos() ??
            self.draw_player()
            self.draw_colors()
            self.draw_obstacles()
            self.draw_grid() # TEMPORARY
            # self.draw_darkness()
            self.draw_flag()
        else: # if it is the end, just draw the endscreen
            self.draw_endscreen()
        pygame.display.update()

if __name__ == "__main__":
    model = Model()
    print(model.color_objs[0].position[0])

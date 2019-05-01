import pygame
import random
import actors
from flag import Flag
from education_screen import *

class Cell(object):
    """ This is an object for each grid cell """
    def __init__(self, cell_coord, grid_coord):
        """Initialize the cell object.

        cell_coord: Tuple of coordinate in pixels
        grid_coord: TUple of coordinate in cells"""
        self.cell_coord = cell_coord # coordinates of upper left corner of cell in pixels, tuple
        self.grid_coord = grid_coord # coordinates of cell in terms of position in grid, tuplel
        self.occupied = False

class Model(object):
    """ Class that holds the state of the entire game """
    def __init__(self, cell_size = (40, 40), grid_size = (46, 23)):
        """Initialize the model.

        cell_size: Tuple of the dimension of each cell in pixels
        grid_size: Tuple of the dimensions of the grid in cells"""

        self.cell_size = cell_size
        self.grid_size = grid_size
        self.screen_size = (self.cell_size[0]*self.grid_size[0],
        self.cell_size[1]*self.grid_size[1]+160)
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
                cell_coord = (i*self.cell_size[0], j*self.cell_size[1]+160)
                self.grid_cells[(i,j)] = Cell(cell_coord, (i, j))

    def choose_flag(self):
        """Randomly choose which flag to play the game with."""
        self.flag = Flag({
            1:"ace",
            2:"alt-lesbian",
            3:"bi",
            4:"intersex",
            5:"l-lesbian",
            6:"nb",
            7:"pan",
            8:"poc",
            9:"pride",
            10:"trans"
            }[random.randint(1, 10)])
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
            obstacle = actors.Obstacle((self.cell_size),coord,type)

            obstacle.make_groups(obstacle, self.obstacles)    # add obstacle to group based on what the obstacle's type is

            self.grid_cells[(x_cell,y_cell)].occupied = True
            self.grid_cells[(x_cell,y_cell)].type = 'obstacle'

    def erase_obstacles(self, key = pygame.K_SPACE):
        """Removes obstacles from self.model.obstacles while spacebar is held"""
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
        """Instantiate Player object"""
        self.player = actors.Player((400, 400), self.screen_size,
        self.obstacles, self.color_objs)

    def make_darkness(self):
        """Instantiate Darkness object"""
        self.darkness = actors.Darkness(self.player, (self.cell_size[0]*self.grid_size[0], self.cell_size[1]*self.grid_size[0]))

    def make_endscreen(self):
        """Instantiate Endscreen object"""
        self.endscreen = EndScreen(self.flag.name, (1920, 1080))

class View():
    """
    Instantiates model and draws the state of every object on the game screen
    """
    def __init__(self, screen_size, filling, model):
        """Initialize model and make game screen"""
        self.model = model
        self.screen = pygame.display.set_mode(screen_size, pygame.FULLSCREEN) # sets screen dimensions
        self.fill_color = filling
        self.screen.fill(self.fill_color) # sets background color
        pygame.display.set_caption('Window Viewer') # sets window caption

    def draw_player(self):
        """Draw the player at its draw position"""
        self.model.player.update_position()
        self.screen.blit(self.model.player.image, self.model.player.get_draw_position())   # places image of player_actor

    def draw_colors(self):
        """Draw the flag colors onto the display"""
        for piece in self.model.color_objs:
            if piece.exists:
                self.screen.blit(piece.image, piece.position)

    def draw_obstacles(self):
        """
        Draw the obstacles on the display

        Ideally the group.draw(self.screen) function would draw both the colored square and the obstacle.png overlay
        """
        for group in self.model.obstacles:       # places image of obstacle for each obstacle created in Model
            for obstacle in group:      # COMMENT OUT THIS FOR LOOP TO TAKE AWAY COLORATION
                color = obstacle.type
                rectangle = pygame.Rect(obstacle.position, self.model.cell_size)
                pygame.draw.rect(self.screen, color, rectangle)     # drawns foundation square of the obstacle's color
            group.draw(self.screen)        # overlays the shaded "spike"
        self.model.erase_obstacles()        # runs method that allows player to erase colored obstacles by holding spacebar

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

    def update(self):
        """Update the draw positons of player, color_actors, obstacles, grid, and the flag"""
        self.screen.fill(self.fill_color)
        if self.model.endgame == False:
            self.draw_player()
            self.draw_colors()
            self.draw_obstacles()
            self.draw_grid() # TEMPORARY
            self.draw_darkness()
            self.draw_flag()
        else: # if it is the end, just draw the endscreen
            self.draw_endscreen()
        pygame.display.update()

class Collision():
    """
    Class to handle collision of obstacles, screen edge, and colors with the player
    """
    def __init__(self, model):
        """Initialize the Collision model.

        model: Model object"""
        self.model = model

    def update(self):
        """Check the collisions for one tick and return if
        there is a collision and what type"""
        # self.check_obstacle_collision()
        # self.check_color_collision()
        self.check_screen_edge()

    def check_screen_edge(self):
        """Prevents the player from leaving any edge of the screen
            switch with screen_wrap based on design preference"""
        if self.model.player.position_c[0] >= self.model.screen_size[0]: # if player's center goes past max x-dimension of screen, they cannot go further
            self.model.player.position_c[0] = self.model.screen_size[0]
        elif self.model.player.position_c[1] >= self.model.screen_size[1]: # if player's center goes past max y-dimension of screen, they cannot go further
            self.model.player.position_c[1] = self.model.screen_size[1]
        elif self.model.player.position_c[0] <= 0: # if player's center goes past min x-dimension of screen, they cannot go further
            self.model.player.position_c[0] = 0
        elif self.model.player.position_c[1] <= 0: # if player's center goes past min y-dimension of screen, they cannot go further
            self.model.player.position_c[1] = 0

    # check collision
    # update?

    # obstacle

    # flag

    # screen

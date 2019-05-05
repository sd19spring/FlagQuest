import pygame
import random
import actors
from flag import Flag
from education_screen import *
from level_generation import *
import copy
import math

class Cell(object):
    """ This is an object for each grid cell """
    def __init__(self, cell_coord, grid_coord):
        """Initialize the cell object.

        cell_coord: Tuple of coordinate in pixels
        grid_coord: TUple of coordinate in cells"""
        self.cell_coord = cell_coord # coordinates of upper left corner of cell in pixels, tuple
        self.label = grid_coord # coordinates of cell in terms of position in grid, tuple
        self.occupied = False
        self.type = "nothing"

class Model(object):
    """ Class that holds the state of the entire game """
    def __init__(self, cell_size = (40, 40), grid_size = (46, 20)):
        """Initialize the model.

        cell_size: Tuple of the dimension of each cell in pixels
        grid_size: Tuple of the dimensions of the grid in cells"""

        self.cell_size = cell_size
        self.grid_size = grid_size
        self.screen_size = (self.cell_size[0]*self.grid_size[0],
        self.cell_size[1]*self.grid_size[1]+160)
        self.endgame = False
        self.obstacles = []
        self.cleared_obstacles = []
        self.make_grid()
        self.choose_flag()
        self.make_colors()
        self.make_player()
        self.generate_level()
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
            10:"trans",
            11:"gqueer"
            }[random.randint(1, 10)])

    def make_colors(self):
        """Instantiate Color objects for each color in the chosen flag."""
        self.color_objs = []
        for color in self.flag.colors:
            # could we have a get random coord method?
            x_cell = random.randint(0, self.grid_size[0]-1)
            y_cell = random.randint(0, self.grid_size[1]-1)
            # coord = self.grid_cells[random_coord]
            # coord = random_coord((0, 0), (self.grid_size))
            cell_coord = self.grid_cells[(x_cell,y_cell)].cell_coord
            grid_coord = self.grid_cells[(x_cell,y_cell)].label
            # coord = (x_cell, y_cell)
            self.color_objs.append(actors.Color(color, self.cell_size, cell_coord, grid_coord, self.grid_cells[grid_coord]))
            self.grid_cells[(x_cell,y_cell)].occupied = True
            self.grid_cells[(x_cell,y_cell)].type = 'color'

    def generate_level(self):
        """Generates playable level"""

        #gets position of player for play path
        player_pos = self.player.position_c
        player_grid_pos = (math.floor((player_pos[0]-40)/self.cell_size[0]), math.floor((player_pos[1] - 160)/self.cell_size[1]))
        player_cell = self.grid_cells[(player_grid_pos)]

        #initializes order of goals for random playable path
        path_order_colors = self.color_objs
        random.shuffle(path_order_colors)
        path_order = [color.cell_in for color in path_order_colors]
        path_order.insert(0,player_cell)

        #generates path, places obstacles accordingly
        self.path = []
        ind = 0
        for i in list(range(len(path_order)-1)):
        #for i in range(2):
            zigzag_path = get_zigzag_path(self.grid_cells, path_order[ind], path_order[ind+1], 3)
            self.place_obstacles(zigzag_path, ind)

            for cell in zigzag_path:
                cell.type == 'none'

            self.path.extend(zigzag_path)
            ind += 1

    def place_obstacles(self, path, ind):
        """ Generate obstacles in the grid
        Path: path between two color stripes on which to only place certain colors
        of obstacles"""

        obstacle_types = self.flag.colors[:ind+1]
        for i in range(round(400/(len(self.flag.colors)))):
            x_cell = random.randint(0, self.grid_size[0]-1)
            y_cell = random.randint(0, self.grid_size[1]-1)
            while self.grid_cells[(x_cell, y_cell)].type == 'obstacle' or self.grid_cells[(x_cell, y_cell)].type == 'path' or self.grid_cells[(x_cell, y_cell)].type == 'color':
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
    def __init__(self, screen_size, image, model):
        """Initialize model and make game screen"""
        self.model = model
        self.screen = pygame.display.set_mode(screen_size, pygame.FULLSCREEN) # sets screen dimensions
        self.image = image.convert() # convert makes the image smaller
        pygame.display.set_caption('Window Viewer') # sets window caption

    def draw_player(self):
        """Draw the player at its draw position"""
        self.model.player.update_position()
        self.screen.blit(self.model.player.image, self.model.player.get_draw_position())   # places image of player_actor

    def draw_colors(self):
        """Draw the flag colors onto the display"""
        flag_image = pygame.transform.scale(pygame.image.load('./images/flag_piece_mask.png'), (40,40))
        for piece in self.model.color_objs:
            if piece.exists:
                self.screen.blit(piece.image, piece.position)
                self.screen.blit(flag_image, piece.position)

    def draw_sparkles(self):
        """ draw sparkles to indicate position of flag colors """
        sparkles_image = pygame.transform.scale(pygame.image.load('./images/sparkles.png'), (40,40))
        for piece in self.model.color_objs:
            if piece.exists:
                self.screen.blit(sparkles_image, piece.position)


    def draw_obstacles(self):
        """
        Draw the obstacles on the display

        Ideally the group.draw(self.screen) function would draw both the colored square and the obstacle.png overlay
        """
        for group in self.model.obstacles:       # places image of obstacle for each obstacle created in Model
            for obstacle in group:
                color = obstacle.type
                rectangle = pygame.Rect(obstacle.position, self.model.cell_size)
                pygame.draw.rect(self.screen, color, rectangle)     # drawns foundation square of the obstacle's color
            group.draw(self.screen)        # overlays the shaded "spike"
        self.model.erase_obstacles()        # runs method that allows player to erase colored obstacles by holding spacebar

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

    def draw_path(self):
        """Draw a created path"""
        #colors = [(255, 255, 255), (255, 0, 0), ( 0, 255, 0), ( 0, 0, 255), (255, 255, 0)]
        for step in self.model.path:
            pygame.draw.rect(self.screen, (255, 255, 255),
                    [step.cell_coord[0], step.cell_coord[1],self.model.cell_size[0],
                    self.model.cell_size[1]])

    def update(self):
        """Update the draw positons of player, color_actors, obstacles, grid, and the flag"""
        self.screen.blit(self.image, (0, 0)) # sets background
        if self.model.endgame == False:
            #self.draw_path()
            self.draw_player()
            self.draw_colors()
            self.draw_obstacles()
            self.draw_darkness()
            self.draw_flag()
            self.draw_sparkles()
        else: # if it is the end, just draw the endscreen
            self.draw_endscreen()
        pygame.display.update()

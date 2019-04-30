import pygame
import os
import random
from flag import Flag
from color_actor import Color_Actor
from obstacles import *
from player_actor import *
from darkness import *
from education_screen import *

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
    def __init__(self, cell_size = 40, grid_size = (46, 23)):
        """
        Initialize the model.

        cell_size: Dimension of each cell in pixels. Cells are square so only one number is passed
        grid_size: Tuple of the dimensions of the grid in cells (x dimension, y dimension) """

        self.obstacles = []              # instantiates a list of all obstacle sprite groups
        self.cleared_obstacles = []
        self.cell_size = cell_size
        self.grid_size = (grid_size)
        self.endgame = False
        self.make_grid()
        self.make_all_flags()
        self.choose_flag()
        self.make_colors()
        self.make_player()
        self.make_obstacles()
        self.make_darkness()

    def make_all_flags(self):
        """Create all flag objects to later choose from."""
        #TODO: modify other functions so this is only called once per play
        dir_path = os.path.dirname(os.path.realpath(__file__))      # dir_path allows us to refer to the current folder of this file

        all_flag_dict = {"ace":[(0,0,0), (163,163,163), (255,255,255),(166,1,191)],
                    "alt-lesbian":[(215,44,0),(239,116,39),(255,152,86),(255,255,255),(209,98,166),(183,85,146),(165,1,98)],
                    "bi":[(215,2,112),(115,79,150),(0,56,168)],
                    "intersex":[(255,216,0),(121,2,170)],
                    "l-lesbian":[(184,0,144),(202,103,164),(227,118,182),(255,255,255),(243,192,221),(215,96,100),(158,40,4)],
                    "nb":[(255,244,51),(255,255,255),(155,89,208),(45,45,45)],
                    "pan":[(255,33,142),(255,214,0),(33,176,254)],
                    "poc":[(0,0,0),(115,86,38),(233,50,34),(239,144,52),(252,228,76),(73,155,47),(23,71,173),(179,67,213)],
                    "pride":[(254,0,0),(255,166,3),(255,255,0),(0,129,2),(22,20,228),(128,0,126)],
                    "trans":[(13, 204, 237),(248, 183, 211),(255, 255, 255)]}

        self.all_flags = []

        for name in all_flag_dict:
            calc_image_names = []
            for n in list(range(len(all_flag_dict[name]))):
                image_name = dir_path + '/images/' + name + "/" + str(n+1) + ".png"
                calc_image_names.append(image_name)
            flag = Flag(name, colors = all_flag_dict[name], image_names = calc_image_names)
            self.all_flags.append(flag)

    def choose_flag(self):
        """ Randomly choose which flag to play the game with """

        # num_flag = random.randint(0,len(self.all_flags)-1)
        num_flag = 2
        self.flag = self.all_flags[num_flag]
        print("You are playing with the " + self.flag.name + " flag")

    def make_colors(self):
        """ Instantiate Color_Actor objects for each color in the chosen flag """
        self.color_objs = []
        for i in range(len(self.flag.colors)):
            x_cell = random.randint(0, self.grid_size[0]-1)
            y_cell = random.randint(0, self.grid_size[1]-1)
            coord = self.grid_cells[(x_cell,y_cell)].cell_coord
            self.color_objs.append(Color_Actor(self.flag.colors[i], self, coord))
            self.grid_cells[(x_cell,y_cell)].occupied = True
            self.grid_cells[(x_cell,y_cell)].type = 'color'


    def make_obstacles(self):
        """ Generate obstacles in the grid """
        obstacle_types = self.flag.colors      # makes list of possible obstacle types based off of the flag's colors

        for i in range(200):     # 10 is arbitrary, we should replace with intentional number later
            x_cell = random.randint(0, self.grid_size[0]-1)        # randomizes location of obstacle
            y_cell = random.randint(0, self.grid_size[1]-1)
            while self.grid_cells[(x_cell, y_cell)].occupied == True:   # re-randomizes location if the location is occupied by a color_obj
                x_cell = random.randint(0, self.grid_size[0]-1)
                y_cell = random.randint(0, self.grid_size[1]-1)

            coord = self.grid_cells[(x_cell,y_cell)].cell_coord
            type = random.choice(obstacle_types)            # randomly chooses this obstacle's type
            obstacle = Obstacle((self.cell_size,self.cell_size),coord,type)

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

    def make_grid(self):
        """ Instantiate grid cells for game map """
        self.grid_cells = {}
        cell_size = (self.cell_size,self.cell_size)
        for i in range(self.grid_size[0]):
            for j in range(self.grid_size[1]):
                cell_coord = (i*self.cell_size, 160+j*self.cell_size)
                self.grid_cells[(i,j)] = Cell(cell_coord, (i, j), False, 'none', (i,j))

    def make_player(self):
        """ Instantiate Player object """
        player_image = pygame.transform.scale(pygame.image.load('./images/character.png'), (40,40))
        self.player = Player_actor((400, 400),player_image, (self.cell_size*self.grid_size[0], self.cell_size*self.grid_size[1]+160),self.obstacles, self.color_objs)

    def make_darkness(self):
        """ Instantiate Darkness object"""
        self.darkness = Darkness(self.player, (self.cell_size*self.grid_size[0], self.cell_size*self.grid_size[0]))

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
        self.screen.blit(self.model.player.image, self.model.player.get_draw_position())   # places image of player_actor
        # print(self.model.player.grid_cell)

    def draw_color_actors(self):
        """Draw the flag colors onto the display"""
        for piece in self.model.color_objs:
            if piece.exists == True:
                pygame.draw.rect(self.screen, piece.color, pygame.Rect(piece.position[0], piece.position[1], self.model.cell_size, self.model.cell_size))


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
            self.draw_player()
            self.draw_color_actors()
            self.draw_obstacles()
            self.draw_grid()
            self.draw_darkness()
            self.draw_flag()
        else: # if it is the end, just draw the endscreen
            self.draw_endscreen()
        pygame.display.update()

if __name__ == "__main__":
    model = Model()
    print(model.color_objs[0].position[0])

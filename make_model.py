"""
This code contains the classes for making a model to hold the state
of the game's objects (like player, each obstacle, the color actors, etc.) as
well as a class to hold information for the state of each cell
"""

from color_actor import Color_Actor
from flag import Flag
from obstacles import *
from player_actor import *
from darkness import *
from education_screen import *
import random
import os

class Model(object):
    """ Class that holds the state of the entire game """
    def __init__(self, cell_size = 40, grid_x_size = 46, grid_y_size = 23):
        self.obstacles = [] # change this to a sprite Group sometime
        self.cell_size = cell_size
        self.grid_x_size = grid_x_size
        self.grid_y_size = grid_y_size
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
                    "gqueer":[(189,123,222),(255,255,255),(74,123,33)],
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
        num_flag = 1
        self.flag = self.all_flags[num_flag]
        print("You are playing with the " + self.flag.name + " flag")

    def make_colors(self):
        """ Instantiate Color_Actor objects for each color in the chosen flag """
        self.color_objs = []
        for i in range(len(self.flag.colors)):
            x_cell = random.randint(0, self.grid_x_size-1)
            y_cell = random.randint(0, self.grid_y_size-1)
            coord = self.grid_cells[(x_cell,y_cell)].cell_coord
            self.color_objs.append(Color_Actor(self.flag.colors[i], self, coord[0], coord[1]))
            self.grid_cells[(x_cell,y_cell)].occupied = True
            self.grid_cells[(x_cell,y_cell)].type = 'color'


    def make_obstacles(self):
        """ Generate obstacles in the grid """
        obstacle_types = {'mountain':(128, 128, 128),'mushroom':(200, 0, 0),'shrub':(0, 128, 0),'tree':(163, 105, 17)}    # these types distinguish which obstacles are affected by which flag stripes
        selected_obstacles = list(obstacle_types)[0:len(self.flag.colors)]    # limits number of obstacle type options to the number of Flag colors
        for i in range(10):     # 10 is arbitrary, we should replace with intentional number later
            x_cell = random.randint(0, self.grid_x_size-1)        # randomizes location of obstacle
            y_cell = random.randint(0, self.grid_y_size-1)
            coord = self.grid_cells[(x_cell,y_cell)].cell_coord
            type = random.choice(selected_obstacles)            # randomly chooses this obstacle's type
            color = obstacle_types[type]                        # finds the color associated with this obstacle's type
            self.obstacles.append(Obstacle((self.cell_size,self.cell_size),coord,type,color)) # change this to sprite Group later

            self.grid_cells[(x_cell,y_cell)].occupied = True
            self.grid_cells[(x_cell,y_cell)].type = 'obstacle'

    def make_grid(self):
        """ Instantiate grid cells for game map """
        self.grid_cells = {}
        cell_size = (self.cell_size,self.cell_size)
        for i in range(self.grid_x_size):
            for j in range(self.grid_y_size):
                cell_coord = (i*self.cell_size, 160+j*self.cell_size)
                self.grid_cells[(i,j)] = Cell(cell_coord, False, 'none')

    def make_player(self):
        """ Instantiate Player object """
        player_image = pygame.transform.scale(pygame.image.load('./character.png'), (40,40))
        self.player = Player_actor((400, 400),player_image, (self.cell_size*self.grid_x_size, self.cell_size*self.grid_y_size+160),self.obstacles, self.color_objs)

    def make_darkness(self):
        """ Instantiate Darkness object"""
        self.darkness = Darkness(self.player, (self.cell_size*self.grid_x_size, self.cell_size*self.grid_x_size))

    def make_endscreen(self):
        """ Instantiate Endscreen object"""
        self.endscreen = EndScreen(self.flag.name, (1920, 1080))

class Cell(object):
    """ This is an object for each grid cell. Unclear if this is going to be useful """
    def __init__(self, cell_coord, occupied, type):
        self.cell_coord = cell_coord
        self.occupied = occupied
        self.type = type

if __name__ == "__main__":
    model = Model()
    print(model.color_objs[0].x)

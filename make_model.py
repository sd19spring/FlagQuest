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
import random
import os

# These dictionaries hold the info for each flag
dir_path = os.path.dirname(os.path.realpath(__file__))      # dir_path allows us to refer to the current folder of this file

bisexual = {
            'colors' : [(215, 2, 112), (115, 79, 150), (0, 56, 168)],
            'name' : 'Bisexual Pride Flag',
            'description' : 'This is the bisexual flag',
            'img_names':[dir_path + '/images/bi/biflag.jpg', dir_path + '/images/bi/biflag.jpg', dir_path + '/images/bi/biflag.jpg'] # need to have same number of images as colors
}

trans = {
        'colors' : [(13, 204, 237), (248, 183, 211), (255, 255, 255)],
        'name' : 'Trans Pride Flag',
        'description': 'This is the trans flag',
        'img_names':[dir_path + '/images/trans/t_blue.png', dir_path + '/images/trans/t_pink.png', dir_path + '/images/trans/t_white.png']  # these paths are dependent on the current locations of the image files, and should be adjusted to allow for variability in the coder's set-up
}

flag_list = ['bi','trans']

class Model(object):
    """ Class that holds the state of the entire game """
    def __init__(self, cell_size = 40, grid_size = 20):
        self.obstacles = [] # change this to a sprite Group sometime
        self.cell_size = cell_size
        self.grid_size = grid_size
        self.make_grid()
        self.choose_flag()
        self.make_colors()
        self.make_player()
        self.make_obstacles()
        self.make_darkness()

    def choose_flag(self):
        """ Randomly choose which flag to play the game with """
        num_flag = random.randint(0,1)
        num_flag = 1
        flag_name = flag_list[num_flag]

        if flag_name == 'trans':
            f_dict = trans
        if flag_name == 'bi':
            f_dict = bisexual

        # img_pieces = [pygame.image.load(image_name) for image_name in f_dict['img_names']]
        #print(img_pieces)
        self.flag = Flag(f_dict['name'], image_names = f_dict['img_names'],
                        colors = f_dict['colors'], description = f_dict['description'])

    def make_colors(self):
        """ Instantiate Color_Actor objects for each color in the chosen flag """
        self.color_objs = []
        for i in range(len(self.flag.colors)):
            x_cell = random.randint(0, self.grid_size-1)
            y_cell = random.randint(0, self.grid_size-1)
            coord = self.grid_cells[(x_cell,y_cell)].cell_coord
            self.color_objs.append(Color_Actor(self.flag.colors[i], self, coord[0], coord[1]))

    def make_obstacles(self):
        """ Generate obstacles in the grid """
        obstacle_types = {'mountain':(128, 128, 128),'mushroom':(200, 0, 0),'shrub':(0, 128, 0),'tree':(163, 105, 17)}    # these types distinguish which obstacles are affected by which flag stripes
        selected_obstacles = list(obstacle_types)[0:len(self.flag.colors)]    # limits number of obstacle type options to the number of Flag colors
        for i in range(10):     # 10 is arbitrary, we should replace with intentional number later
            x_cell = random.randint(0, self.grid_size-1)        # randomizes location of obstacle
            y_cell = random.randint(0, self.grid_size-1)
            coord = self.grid_cells[(x_cell,y_cell)].cell_coord
            type = random.choice(selected_obstacles)            # randomly chooses this obstacle's type
            color = obstacle_types[type]                        # finds the color associated with this obstacle's type
            self.obstacles.append(Obstacle((self.cell_size,self.cell_size),coord,type,color)) # change this to sprite Group later

    def make_grid(self):
        """ Instantiate grid cells for game map """
        self.grid_cells = {}
        cell_size = (self.cell_size,self.cell_size)
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                cell_coord = (i*self.cell_size, j*self.cell_size)
                self.grid_cells[(i,j)] = Cell(cell_coord, False, 'none')

    def make_player(self):
        """ Instantiate Player object """
        player_image = pygame.image.load('./images/player2.png')
        self.player = Player_actor((10, 10),player_image, (self.cell_size*self.grid_size, self.cell_size*self.grid_size))

    def make_darkness(self):
        """ Instantiate Darkness object"""
        self.darkness = Darkness(self.player, (self.cell_size*self.grid_size, self.cell_size*self.grid_size), 90)

class Cell(object):
    """ This is an object for each grid cell. Unclear if this is going to be useful """
    def __init__(self, cell_coord, occupied, type):
        self.cell_coord = cell_coord
        self.occupied = occupied
        self.type = type

if __name__ == "__main__":
    model = Model()
    print(model.color_objs[0].x)

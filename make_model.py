from color_actor import Color_Actor
from flag_class import Flag
from obstacles import *
from player_actor import *
import random

bisexual = {
            'colors' : [(215, 2, 112), (115, 79, 150), (0, 56, 168)],
            'name' : 'Bisexual Pride Flag',
            'description' : 'This is the bisexual flag',
            'img_names':['biflag.jpg', 'biflag.jpg', 'biflag.jpg'] # need to have same number of images as colors
}

trans = {
        'colors' : [(13, 204, 237), (248, 183, 211), (255, 255, 255)],
        'name' : 'Trans Pride Flag',
        'description': 'This is the trans flag',
        'img_names':['tg blue.png', 'tg pink.png', 'tg white.png']
}

flag_list = ['bi','trans']

class Model(object):
    def __init__(self, cell_size = 40, grid_size = 20):
        self.obstacles = [] # change this to a sprite Group sometime
        self.cell_size = cell_size
        self.grid_size = grid_size
        self.make_grid()
        self.choose_flag()
        self.make_colors()
        self.make_player()
        self.make_obstacles()

    def choose_flag(self):
        num_flag = random.randint(0,1)
        flag_name = flag_list[num_flag]

        if flag_name == 'trans':
            f_dict = trans
        if flag_name == 'bi':
            f_dict = bisexual

        img_pieces = [pygame.image.load(image_name) for image_name in f_dict['img_names']]
        #print(img_pieces)
        self.flag = Flag(f_dict['name'], image_pieces = img_pieces,
                        colors = f_dict['colors'], description = f_dict['description'])

    def make_colors(self):
        self.color_objs = []
        for i in range(len(self.flag.colors)):
            x_cell = random.randint(0, self.grid_size-1)
            y_cell = random.randint(0, self.grid_size-1)
            coord = self.grid_cells[(x_cell,y_cell)].cell_coord
            self.color_objs.append(Color_Actor(self.flag.colors[i], coord[0], coord[1]))

    def make_obstacles(self):
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
        self.grid_cells = {}
        cell_size = (self.cell_size,self.cell_size)
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                cell_coord = (i*self.cell_size, j*self.cell_size)
                self.grid_cells[(i,j)] = Cell(cell_coord, False, 'none')

    def make_player(self):
        player_image = pygame.image.load('./images/player2.png')
        self.player = Player_actor(10,10,player_image)

class Cell(object):
    def __init__(self, cell_coord, occupied, type):
        self.cell_coord = cell_coord
        self.occupied = occupied
        self.type = type


model = Model()
print(model.color_objs[0].x)

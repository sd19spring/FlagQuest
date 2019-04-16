from color_actor import Color_Actor
from flag_class import Flag
from obstacles import *
import random

bisexual = {
            'colors' : [(215, 2, 112), (115, 79, 150), (0, 56, 168)],
            'name' : 'Bisexual Pride Flag',
            'description' : 'This is the bisexual flag'
}

trans = {
        'colors' : [(13, 204, 237), (248, 183, 211), (255, 255, 255)],
        'name' : 'Trans Pride Flag',
        'description': 'This is the trans flag',
        'img_names':['tg blue.png', 'tg pink.png', 'tg white.png']
}

flag_list = ['trans']

class Model(object):
    def __init__(self):
        self.choose_flag()
        self.make_colors()
        self.obstacles = [] # change this to a sprite Group sometime

    def choose_flag(self):
        num_flag = 0
        flag_name = flag_list[num_flag]

        if flag_name == 'trans':
            f_dict = trans

        img_pieces = [pygame.image.load(image_name) for image_name in f_dict['img_names']]
        print(img_pieces)
        self.flag = Flag(f_dict['name'], image_pieces = img_pieces,
                        colors = f_dict['colors'], description = f_dict['description'])

    def make_colors(self):
        self.color_objs = []
        for i in range(len(self.flag.colors)):
            x = random.randint(0, 640)
            y = random.randint(0, 400)
            self.color_objs.append(Color_Actor(self.flag.colors[i], x, y))

    def make_obstacles(self):
        obstacle_types = ['mountain','river','shrub','tree']    # these types distinguish which obstacles are affected by which flag stripes
        for i in range(10):     # 10 is arbitrary, we should replace with intentional number later
            x = random.randint(0, 640)
            y = random.randint(0, 400)
            type = random.choice(obstacle_types)
            self.obstacles.append(Obstacle((50,50),(x,y),type)) # change this to sprite Group later


model = Model()
print(model.color_objs[0].x)

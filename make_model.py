from color_actor import Color_Actor
from flag_class import Flag
from obstacles import *
import random

bisexual = {
            'colors' : [(215, 2, 112), (115, 79, 150), (0, 56, 168)],
            'name' : 'Bisexual Pride Flag',
            'description' : 'This is the bisexual flag'
}

class Model(object):
    def __init__(self):
        self.choose_flag()
        self.make_colors()
        self.obstacles = [] # change this to a sprite Group sometime

    def choose_flag(self):
        num_flag = 1

        if num_flag == 1:
            self.colors = bisexual['colors']
            self.name = bisexual['name']
            self.description = bisexual['description']

    def make_colors(self):
        self.color_objs = []
        for i in range(len(self.colors)):
            x = random.randint(0, 640)
            y = random.randint(0, 400)
            self.color_objs.append(Color_Actor(self.colors[i], x, y))

    def make_obstacles(self):
        obstacle_types = ['mountain','river','shrub','tree']    # these types distinguish which obstacles are affected by which flag stripes
        for i in range(10):     # 10 is arbitrary, we should replace with intentional number later
            x = random.randint(0, 640)
            y = random.randint(0, 400)
            type = random.choice(obstacle_types)
            self.obstacles.append(Obstacle((50,50),(x,y),type)) # change this to sprite Group later


model = Model()
print(model.color_objs[0].x)

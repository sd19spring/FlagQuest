from color_actor import Color_Actor
from flag_class import Flag
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

model = Model()
print(model.color_objs[0].x)

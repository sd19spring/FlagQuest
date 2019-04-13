import pygame
import time
from player_actor import *
from controller import *
from make_model import Model

class View():
    def __init__(self, width, height, filling, model):
        self.model = model
        self.screen = pygame.display.set_mode((width, height))  # sets screen dimensions
        self.screen.fill(filling)        # sets background color
        pygame.display.set_caption('Window Viewer')             # sets window caption
        #pygame.display.flip()            # updates contents of entire display

    def draw_player(self):
        pass

    def draw_color_actors(self):
        for i in range(len(self.model.color_objs)):
            pygame.draw.circle(self.screen,
                               pygame.Color(self.model.colors[i][0], self.model.colors[i][1], self.model.colors[i][2]),
                               [self.model.color_objs[i].x,
                               self.model.color_objs[i].y],
                               10)
        pass

    def draw_obstacles(self):
        pass

    def update(self):
        self.draw_color_actors()

        pygame.display.update()


#window = pygame.display.set_mode((640, 400))
#window.fill((144, 238, 144))    # a painfully bright tone of green

#BLUE = (0, 0, 255)
#buddy = Player_actor(10,20,90,BLUE,width = 50, height = 70)

#def update():
#    buddy.get_keypress()
#    buddy.move()
#    buddy.draw(window)
#    time.sleep(.01)

def play_game(size):
    pygame.init()

    model = Model()
    view = View(size[0], size[1], (0, 0, 0), model)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        view.update()
        time.sleep(0.1)

if __name__ == '__main__':


    size = (640,400)
    play_game(size) # start running game

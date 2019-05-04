import pygame
import time
import gameworld
from pygame.locals import *
from controller import *
from flag import Flag
from level_generation import *

class Game():
    """Class to manage the actor and gameworld classes"""
    def __init__(self, size=(1880,1080), image=pygame.image.load('images/background.png')):
        """Create the world.

        size: Tuple of the window dimensions
        image: Background image"""
        self.image = pygame.transform.scale(image, size)
        self.model = gameworld.Model()
        self.view = gameworld.View(size, self.image, self.model)
        self.running = True

    def check_events(self):
        """Check the events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False # close the game
            elif event.type == KEYDOWN and self.model.endgame == True:
                self.model.endscreen.pressed(event.key) # flip pages
                if event.key is pygame.K_SPACE: # if space pressed
                    self.running = False # close the game
            if event.type == KEYDOWN and event.key is pygame.K_ESCAPE: # if escape is pressed
                pygame.display.toggle_fullscreen()

    def check_collision(self):
        """Check for collisions between the player and screen objects"""
        touched_piece = self.model.player.check_color_collision(self.model.color_objs)
        if touched_piece:
            touched_piece.exists = False # makes the touched piece disappear
            self.model.flag.add_color(touched_piece) # add stripe to the flag graphic
            if self.model.flag.complete() == True:
                self.model.make_endscreen()
                self.model.endgame = True

    def update(self):
        """Updates the game for one tick"""
        self.check_events()
        self.check_collision()
        self.view.update()
        time.sleep(0.01)

class StartScreen():
    """Class to manage the start screen"""
    def __init__(self, image=pygame.image.load('images/menu.png')):
        self.screen = pygame.display.set_mode(image.get_size(), pygame.RESIZABLE) # sets screen dimensions
        self.image = image.convert() # convert makes the image easier to draw smaller
        self.running = True
        self.game_start = False

    def check_events(self):
        """Check for key presses"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False # close the game
            if event.type == KEYDOWN and event.key is pygame.K_SPACE: # if space pressed
                self.game_start = True # close the game

    def update(self):
        """Update the start screen"""
        self.check_events()
        self.screen.blit(self.image, (0, 0)) # sets background
        pygame.display.update()
        time.sleep(0.01)

def start_game():
    menu = StartScreen()
    while menu.running:
        menu.update()
        if menu.game_start:
            menu.running = False
            menu.game_start = False
            play_game()

def play_game():
    game = Game()
    while game.running:
        game.update()

if __name__ == '__main__':
    start_game()

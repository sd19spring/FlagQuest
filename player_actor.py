import pygame
from pygame import transform
import time
from controller import Keyboard_Controller as controller

class Player_actor(pygame.sprite.Sprite):
    """
    allows you to make a player character who you control to move around the world
    """
    def __init__(self, pos, image, screen_size):
        """
        Initialize the player

        pos: a tuple of the starting position of the player
        image: the image file for the player
        screen_size: a tuple of the screen dimensions
        """
        pygame.sprite.Sprite.__init__(self) # set up the actor's spriteness

        self.image = image
        self.image_orig = self.image # sets an original copy of the image to reference later
        self.player_size = self.image.get_size()    # player_size is a tuple representing the image's dimensions
        self.position_c = [pos[0] + pos[0]/2, pos[1] + pos[1]/2] # find the center of the image
        self.cont = controller(2) # initialize controller with 2 max velocity
        self.screen_size = screen_size   # refers to screen size

    def __str__(self):
        return "Player centered at location %s with a %d-degree heading. The sprite's dimensions are %dx%d" % (self.position_c, self.cont.angle, self.player_size[0], self.player_size[1])

    def get_keypress(self):
        """Adjusts the player_actor's velocity depending on which arrowkeys are pressed"""
        self.cont.pressed(pygame.key.get_pressed())

    def check_screen_wrap(self):
        """Checks if player has left the screen"""
        if self.position_c[0] > self.screen_size[0]:   # if player's center goes past max x-dimension of screen, wrap to the min x-dimension of screen
            self.position_c[0] = 0
        elif self.position_c[1] > self.screen_size[1]:   # if player's center goes past max y-dimension of screen, wrap to the min y-dimension of screen
            self.position_c[1] = 0
        elif self.position_c[0] < 0:              # if player's center goes past min x-dimension of screen, wrap to the max x-dimension of screen
            self.position_c[0] = self.screen_size[0]
        elif self.position_c[1] < 0:              # if player's center goes past min y-dimension of screen, wrap to the max y-dimension of screen
            self.position_c[1] = self.screen_size[1]


    def move(self, step_size = 1):      # step size adjusts how many pixels the player_actor moves at a time
        """Moves the player."""
        self.position_c[0] += self.cont.v_x*step_size
        self.position_c[1] += self.cont.v_y*step_size
        self.check_screen_wrap()

    def update_draw_position(self):
        """Finds the position to draw the player at. Based on if moving at a 45 or 90 degree angle"""
        if self.cont.v_x != 0 and self.cont.v_y != 0: # If moving at an angle
            self.position_d = (self.position_c[0] - 3*self.player_size[0]/4, self.position_c[1] - 3*self.player_size[0]/4) # translates centered dimensions to account for 45 degree movement
        else: # if standing still or moving at 90 degrees
            self.position_d = (self.position_c[0] - self.player_size[0]/2, self.position_c[1] - self.player_size[1]/2)    # translates centered dimensions back to top-left corner dimensions

    def update_position(self):
        """Update the image based on the facing of the player"""
        self.get_keypress()         # recieve keyboard input
        self.move(step_size=1)      # adjust character position based on arrowkey presses
        self.cont.facing()          # Updates the facing postition
        self.image = transform.rotate(self.image_orig, self.cont.angle) # rotates the image
        self.update_draw_position()
if __name__ == "__main__":
    player_image = pygame.image.load('./images/player2.png')
    buddy = Player_actor((10,20),player_image,(800, 800))
    print(buddy)

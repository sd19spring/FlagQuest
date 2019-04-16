import pygame
from pygame import transform
import time
from controller import Keyboard_Controller as controller

class Player_actor(pygame.sprite.Sprite):
    """
    allows you to make a player character who you control to move around the world
    """
    def __init__(self, x_pos, y_pos, start_angle, image, width, height):
        """
        initialize the player_actor character
        depends upon facing from controller
        image is the graphic image that makes the player
        width and height are in regards to its size and shape
        """
        pygame.sprite.Sprite.__init__(self) # set up the actor's spriteness

        self.x_pos = x_pos
        self.y_pos = y_pos
        self.dimensions = width, height
        self.cont = controller(2) # 2 is the max velocity
        self.cont.angle = start_angle       # 4/13/19 facing has yet to be implimented

        self.image = image
        self.image_orig = self.image # sets an original copy of the image to reference later


    def __str__(self):
        return "Player centered at location (%d, %d) with a %d-degree heading. The sprite's dimensions are %dx%d" % (self.x_pos, self.y_pos, self.facing, self.dimensions[0], self.dimensions[1])

    def get_keypress(self):
        """Adjusts the player_actor's velocity depending on which arrowkeys are pressed"""
        self.cont.pressed(pygame.key.get_pressed())

    def move(self, step_size = 1):      # step size adjusts how many pixels the player_actor moves at a time
        self.x_pos += self.cont.v_x*step_size
        self.y_pos += self.cont.v_y*step_size
        self.position = self.x_pos, self.y_pos  # updates position to reflect the movement due to keyboard input

    def update_image(self):
        """Update the image based on the facing of the player"""
        self.get_keypress()         # recieve keyboard input
        self.move(step_size=1)      # adjust character position based on arrowkey presses
        self.cont.facing()          # Updates the facing postition
        self.image = transform.rotate(self.image_orig, self.cont.angle) # rotates the image

if __name__ == "__main__":
    player_image = pygame.image.load('./images/player2.png')
    buddy = Player_actor(10,20,90,player_image,width = 5, height = 7)
    print(buddy)

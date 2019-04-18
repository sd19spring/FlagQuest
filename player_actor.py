import pygame
from pygame import transform
import time
from controller import Keyboard_Controller as controller

class Player_actor(pygame.sprite.Sprite):
    """
    allows you to make a player character who you control to move around the world
    """
    def __init__(self, x_pos, y_pos, image):
        """
        initialize the player_actor character
        depends upon facing from controller
        x_pos and y_pos refer to the coordinates of the top-left corner of player
        image is the graphic image that makes the player
        """
        pygame.sprite.Sprite.__init__(self) # set up the actor's spriteness


        self.image = image
        self.image_orig = self.image # sets an original copy of the image to reference later
        self.player_size = self.image.get_size()    # player_size is a tuple representing the image's dimensions
        self.position = (x_pos, y_pos)
        self.x_c = self.position[0] + self.player_size[0]/2    # uses x-component of image dimension to find the x-coordinate of the player's center
        self.y_c = self.position[1] + self.player_size[1]/2    # uses y-component of image dimension to find the y-coordinate of the player's center
        # self._get_center()
        self.cont = controller(2) # 2 is the max velocity

        self.screen_size = (800,800)   # refers to screen size

    def __str__(self):
        return "Player centered at location (%d, %d) with a %d-degree heading. The sprite's dimensions are %dx%d" % (self.x_c, self.y_c, self.facing, self.player_size[0], self.player_size[1])

    def _get_positions(self):
        # position
        # center position
        # update position (depends on how we are moving)
        # test extreme positions than dial in
        pass

    def get_keypress(self):
        """Adjusts the player_actor's velocity depending on which arrowkeys are pressed"""
        self.cont.pressed(pygame.key.get_pressed())

    def move(self, step_size = 1):      # step size adjusts how many pixels the player_actor moves at a time
        self.x_c += self.cont.v_x*step_size
        self.y_c += self.cont.v_y*step_size

        if self.x_c > self.screen_size[0]:   # if player's center goes past max x-dimension of screen, wrap to the min x-dimension of screen
            self.x_c = 0
        elif self.y_c > self.screen_size[1]:   # if player's center goes past max y-dimension of screen, wrap to the min y-dimension of screen
            self.y_c = 0
        elif self.x_c < 0:              # if player's center goes past min x-dimension of screen, wrap to the max x-dimension of screen
            self.x_c = self.screen_size[0]
        elif self.y_c < 0:              # if player's center goes past min y-dimension of screen, wrap to the max y-dimension of screen
            self.y_c = self.screen_size[1]

        self.position_c = self.x_c, self.y_c  # updates position to reflect the movement due to keyboard input
        self.position = (self.position_c[0] - self.player_size[0]/2, self.position_c[1] - self.player_size[1]/2)    # translates centered dimensions back to top-left corner dimensions

    def update_image(self):
        """Update the image based on the facing of the player"""
        self.get_keypress()         # recieve keyboard input
        self.move(step_size=1)      # adjust character position based on arrowkey presses
        self.cont.facing()          # Updates the facing postition
        self.image = transform.rotate(self.image_orig, self.cont.angle) # rotates the image

if __name__ == "__main__":
    player_image = pygame.image.load('./images/player2.png')
    buddy = Player_actor(10,20,player_image)
    print(buddy)

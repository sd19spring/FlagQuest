import pygame
from pygame import transform
import time
from controller import Keyboard_Controller as controller

class Player_actor(pygame.sprite.Sprite):
    """
    sprite
    position
    handle movement
    """
    def __init__(self, x_pos, y_pos, start_angle, filling, width, height):
        """
        initialize the player_actor character
        depends upon facing from controller
        filling is what the character visually looks like (for now it's just a color)
        width and height are in regards to its size and shape
        """
        pygame.sprite.Sprite.__init__(self) # set up the actor's spriteness

        self.x_pos = x_pos
        self.y_pos = y_pos
        self.dimensions = width, height
        self.cont = controller(2) # 2 is the max velocity
        self.cont.angle = start_angle       # 4/13/19 facing has yet to be implimented

        # self.image = pygame.Surface(self.dimensions)    # sets size of sprite's visual representation
        # self.image.fill('./images/player.jpg')    # this just fills it with a color, later it will actually be an image
        self.image = pygame.image.load('./images/player.jpg')
        self.image_orig = self.image # sets an original copy of the image to reference later
        # self.shape = self.image.get_rect()    # we don't need this rn (4/13/19), maybe it's important for the future though?

    def __str__(self):
        return "Player centered at location (%d, %d) with a %d-degree heading. The sprite's dimensions are %dx%d" % (self.x_pos, self.y_pos, self.facing, self.dimensions[0], self.dimensions[1])

    def get_keypress(self):
        """Adjusts the player_actor's velocity depending on which arrowkeys are pressed"""
        key = pygame.key.get_pressed()
        self.cont.pressed(key)

    def update_image(self):
        """Update the image based on the facing of the player"""
        self.cont.facing() # Updates the facing postition
        self.image = transform.rotate(self.image_orig, self.cont.angle) # rotates the image

    def draw(self, screen):
        """Blits the screen with the player_actor at its position (i.e. x_pos,y_pos)"""
        self.update_image()
        screen.blit(self.image, self.position)   # places image of player_actor

    def move(self, step_size = 1):      # step size adjusts how many pixels the player_actor moves at a time
        self.x_pos += self.cont.v_x*step_size
        self.y_pos += self.cont.v_y*step_size
        self.position = self.x_pos, self.y_pos  # updates position to reflect the movement due to keyboard input

if __name__ == "__main__":
    BLUE = (0, 0, 255)
    buddy = Player_actor(10,20,90,BLUE,width = 5, height = 7)
    print(buddy)

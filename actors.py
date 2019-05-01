import pygame
from pygame import transform
import time
import numpy
from controller import Keyboard_Controller as controller


def make_image(color, size):
    """Makes a rectangular image.

    color: Tuple of the RGB color code
    size: Tuple of the size of the image in pixels

    returns: image"""
    image = pygame.Surface(size)
    image.fill(color)
    return image

def cell_to_pixel():
    """Converts cell coordinates to pixel coordinates"""
    # this could be used for drawing stuff
    pass

class Actor():
    """
    The Actor class contains generic information which can be inherinted by all actors.
    """
    def __init__(self, image, size, position):
        """Initialize the actor.

        image: image file of the actor
        size: Tuple of the size of the actor in pixels
        position: Tuple of the position of the actor in pixels
        """
        # pygame.sprite.Sprite.__init__(self) # set up the actor's spriteness
        self.size = size
        self.image = pygame.transform.scale(image, self.size)
        self.position = position
        self.get_rect()


    def get_rect(self):
        """Get the rectangle for the Actor"""
        self.rect = self.image.get_rect(topleft = self.position)

class Color(Actor):
    """
    The Color class contains the state and sprite
    of each color of the flag.
    """
    def __init__(self, color, size, position):
        """Initialize the Color_Actor object

        color: Tuple of the RGB color code
        size: Tuple of the size in pixels
        position: Tuple of the position in pixels
        """
        image = make_image(color, size)
        super(Color, self).__init__(image, size, position)
        self.exists = True      # used in make_model to make actor disappear if collided with
        self.color = color

# SCREEN EDGES SHOULD BE HANDLED ELSEWHERE
# OBSTACLE COLLISION SHOULD BE HANDLED LSEWHERE
# COLOR COLLISION SHOULD BE HANDLED ELSEWHEER
class Player(Actor):
    """
    The Player class contains methods specific
    to the playable character.
    """
    def __init__(self, pos, screen_size, obstacles, color_objs, size = (40, 40),
    image = pygame.image.load('./images/character.png')):
        """
        Initialize the player

        pos: a tuple of the starting position of the player
        image: the image file for the player
        screen_size: a tuple of the screen dimensions
        obstacles: brings in a list of all obstacles on map
        """
        super(Player, self).__init__(image, size, pos)
        # pygame.sprite.Sprite.__init__(self) # set up the actor's spriteness

        # self.size = self.image.get_size()    # size is a tuple representing the image's dimensions
        self.get_rotations()
        self.position_c = [pos[0] + pos[0]/2, pos[1] + pos[1]/2] # find the center of the image
        self.grid_cell = (numpy.rint(self.position_c[0]/40), numpy.rint(self.position_c[1]/40))
        self.screen_size = screen_size   # refers to screen size
        # self.rect = pygame.Rect(self.position_c[0] - self.size[0]/2,
        #             self.position_c[1] - self.size[1]/2,
        #             self.size[0], self.size[1])

        self.cont = controller(max_velocity = 10)       # initialize velocity of player

        self.collided_with = []
        self.obstacles = obstacles
        self.color_objs = color_objs

    def __str__(self):
        return "Player centered at location %s with a %d-degree heading. The sprite's dimensions are %s" % (self.position_c, self.cont.angle, str(self.size))

    def get_rotations(self):
        """Get all the rotations for the player image"""
        self.rotations = {
        0:transform.rotate(self.image, 0),
        45:transform.rotate(self.image, 45),
        90:transform.rotate(self.image, 90),
        135:transform.rotate(self.image, 135),
        180:transform.rotate(self.image, 180),
        225:transform.rotate(self.image, 225),
        270:transform.rotate(self.image, 270),
        315:transform.rotate(self.image, 315)}

    def get_keypress(self):
        """Adjusts the player_actor's velocity depending on which arrowkeys are pressed"""
        self.cont.pressed(pygame.key.get_pressed())

    def screen_wrap(self):
        """If player has left one edge of screen, they appear on the other edge
            switch with screen_wall based on design preference"""
        if self.position_c[0] > self.screen_size[0]:   # if player's center goes past max x-dimension of screen, wrap to the min x-dimension of screen
            self.position_c[0] = 0
        elif self.position_c[1] > self.screen_size[1]:   # if player's center goes past max y-dimension of screen, wrap to the min y-dimension of screen
            self.position_c[1] = 0
        elif self.position_c[0] < 0:              # if player's center goes past min x-dimension of screen, wrap to the max x-dimension of screen
            self.position_c[0] = self.screen_size[0]
        elif self.position_c[1] < 0:              # if player's center goes past min y-dimension of screen, wrap to the max y-dimension of screen
            self.position_c[1] = self.screen_size[1]

    def screen_wall(self):
        """Prevents the player from leaving any edge of the screen
            switch with screen_wrap based on design preference

            BUG: player can escape through the corners of screen!!
            """
        if self.position_c[0] >= self.screen_size[0]:   # if player's center goes past max x-dimension of screen, they cannot go further
            self.position_c[0] = self.screen_size[0]
        elif self.position_c[1] >= self.screen_size[1]:   # if player's center goes past max y-dimension of screen, they cannot go further
            self.position_c[1] = self.screen_size[1]
        elif self.position_c[0] <= 0:              # if player's center goes past min x-dimension of screen, they cannot go further
            self.position_c[0] = 0
        elif self.position_c[1] <= 0:              # if player's center goes past min y-dimension of screen, they cannot go further
            self.position_c[1] = 0


    def move(self):      # step size adjusts how many pixels the player_actor moves at a time
        """Moves the player."""
        self.position_c[0] += self.cont.v_x
        self.position_c[1] += self.cont.v_y
        self.screen_wall()  # for this version, we implimented the screen_wall function, which prevents the player from exiting the on-screen map

    def get_draw_position(self):
        """Finds the position to draw the player at. Based on if moving at a 45 or 90 degree angle"""
        if self.cont.v_x != 0 and self.cont.v_y != 0: # If moving at an angle
            return (self.position_c[0] - 3*self.size[0]/4, self.position_c[1] - 3*self.size[0]/4) # translates centered dimensions to account for 45 degree movement
        else: # if standing still or moving at 90 degrees
            return (self.position_c[0] - self.size[0]/2, self.position_c[1] - self.size[1]/2)    # translates centered dimensions back to top-left corner dimensions

    def update_position(self):
        """Update the image based on the facing of the player"""
        self.get_keypress()         # recieve keyboard input
        self.move()
        self.check_obstacle_collision()     # bumps player if they hit an obstacle
        self.cont.facing()          # Updates the facing postition
        self.image = self.rotations[self.cont.angle] # grabs the rotated imagex
        self.grid_cell = (numpy.rint(self.position_c[0]/40), numpy.rint(self.position_c[1]/40))


    def update_rect(self):
        """Updates rect boundary, for use in collision detection"""
        self.rect = pygame.Rect(self.position_c[0] - self.size[0]/2,
                    self.position_c[1] - self.size[1]/2,
                    self.size[0], self.size[1])

    def check_obstacle_collision(self):
        """Returns sprite collided with, of obstacle objects, or None if no collisions."""
        angle_bumps = {0:(-1,0), 45:(-1,1), 90:(0,1), 135:(1,1), 180:(1,0), 225:(1,-1), 270:(0,-1), 315:(-1,-1)}

        a = self.cont.v_max      # this multiplier scales the magnitude of collision-bumping to the magnitude of the player's movement

        for group in self.obstacles:
            collision = pygame.sprite.spritecollide(self, group, dokill = False)   # creates list of all obstacles that the player is colliding with

            if len(collision) > 0:      # if the sprite is colliding with any obstacles
                self.position_c[0] += angle_bumps[self.cont.angle][0]*a      # moves the sprite in the opposite direction of their facing
                self.position_c[1] += angle_bumps[self.cont.angle][1]*a

    def check_color_collision(self, color_objs):
        """Returns sprite collided with, of color objects, or None if no collisions.
        Keeps track of what collisions have already happened, and does not repeat collisions"""
        self.update_rect()

        collision = pygame.sprite.spritecollideany(self, color_objs)
        if collision:
            if collision not in self.collided_with:
                self.collided_with.append(collision)
                print(collision)
                return collision

#class Darkness(Actor)

""" This file has the classes for Color, Player, and Obstacle actors """

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

class Actor():
    """
    The Actor class contains generic information which can be inherinted by all actors.
    """
    def __init__(self, image, size, position = (0, 0)):
        """Initialize the actor.

        image: image file of the actor
        size: Tuple of the size of the actor in pixels
        position: Tuple of the position of the actor in pixels
        """
        # pygame.sprite.Sprite.__init__(self) # set up the actor's spriteness
        self.size = size
        self.position = position
        if type(image) != list:     # this exception is to leave room for obstacle class to define its own self.image and self.rect
            self.image = pygame.transform.scale(image, self.size)
            self.rect = self.image.get_rect(topleft = self.position)

    def get_rotations(self, image_flipped=None):
        """Get all the rotations for the actor image

        image_flipped: Optional Image file for a flipped
        version"""
        if image_flipped != None: # if image_flipped exists
            self.rotations = {
            0:transform.rotate(self.image, 0),
            45:transform.rotate(self.image, 45),
            90:transform.rotate(self.image, 90),
            135:transform.rotate(image_flipped, 315),
            180:transform.rotate(image_flipped, 0),
            225:transform.rotate(image_flipped, 45),
            270:transform.rotate(image_flipped, 90),
            315:transform.rotate(self.image, 315)}
        else:
            self.rotations = {
            0:transform.rotate(self.image, 0),
            45:transform.rotate(self.image, 45),
            90:transform.rotate(self.image, 90),
            135:transform.rotate(self.image, 135),
            180:transform.rotate(self.image, 180),
            225:transform.rotate(self.image, 225),
            270:transform.rotate(self.image, 270),
            315:transform.rotate(self.image, 315)}

class Color(Actor):
    """
    The Color class contains the state and sprite
    of each color of the flag.
    """
    def __init__(self, color, size, position, grid_cell, cell_in):
        """Initialize the Color_Actor object

        color: Tuple of the RGB color code
        size: Tuple of the size in pixels
        position: Tuple of the position in pixels
        """
        image = make_image(color, size)
        super(Color, self).__init__(image, size, position)
        self.exists = True      # used in make_model to make actor disappear if collided with
        self.color = color
        self.label = grid_cell
        self.cell_in = cell_in

class Darkness(Actor):
    """
    Creates a black cover up to cover the screen
    """
    def __init__(self, player, screen_size,
    image = pygame.image.load('./images/flashlight.png')):
        """Initialize the darkness

        player: a player object
        screen_size: a tuple of the screen dimensions
        image: image file of the darkness
        """
        size = (int(screen_size[0]*2.5), int(screen_size[1]*2.5))
        super(Darkness, self).__init__(image, size)
        self.player = player
        self.get_rotations()

    def __str__(self):
        return "Darkness origin at location %s." % (self.player.position_c)

    def rotate(self):
        """Rotates the darkness to match the player"""
        angle = self.player.cont.angle
        self.image = self.rotations[angle] # overlay image of darkess that points in same direction as player

    def draw_position(self):
        """Finds the draw position for the darkness based on player position"""
        player_c = self.player.position_c
        if self.player.cont.angle%90 == 0: # if on 90 degree increments
            return (player_c[0]-self.size[0]/2, player_c[1]-self.size[1]/2)
        else: # if on 45 degree increments
            a = .21
            return (player_c[0]-self.size[0]/2-self.size[0]*a, player_c[1]-self.size[1]/2-self.size[1]*a)


class Player(Actor):
    """
    The Player class contains methods specific
    to the playable character.
    """
    def __init__(self, pos, screen_size, obstacles, color_objs,
    size = (30, 30), image = pygame.image.load('./images/character.png'),
    image_flipped = pygame.image.load('./images/character_flipped.png')):
        """
        Initialize the player

        pos: a tuple of the starting position of the player
        image: the image file for the player
        screen_size: a tuple of the screen dimensions
        obstacles: brings in a list of all obstacles on map
        """
        super(Player, self).__init__(image, size)
        self.get_rotations(pygame.transform.scale(image_flipped, self.size))
        self.position_c = [pos[0] + pos[0]/2, pos[1] + pos[1]/2] # find the center of the image
        self.grid_cell = (numpy.rint(self.position_c[0]/40), numpy.rint(self.position_c[1]/40))
        self.screen_size = screen_size   # refers to screen size

        self.cont = controller(max_velocity = 10)       # initialize velocity of player

        self.collided_with = []
        self.obstacles = obstacles
        self.color_objs = color_objs

    def __str__(self):
        return "Player centered at location %s with a %d-degree heading. The sprite's dimensions are %s" % (self.position_c, self.cont.angle, str(self.size))

    def get_keypress(self):
        """Adjusts the player_actor's velocity depending on which arrowkeys are pressed"""
        self.cont.pressed(pygame.key.get_pressed())

    def move(self):      # step size adjusts how many pixels the player_actor moves at a time
        """Moves the player."""
        self.position_c[0] += self.cont.v_x
        self.position_c[1] += self.cont.v_y
        self.screen_wall()

    def screen_wall(self):
        """Check
        Prevents the player from leaving any edge of the screen
        switch with screen_wrap based on design preference
        """
        if self.position_c[0] >= self.screen_size[0]: # if player's center goes past max x-dimension of screen, they cannot go further
            self.position_c[0] = self.screen_size[0]
        elif self.position_c[1] >= self.screen_size[1]: # if player's center goes past max y-dimension of screen, they cannot go further
            self.position_c[1] = self.screen_size[1]
        elif self.position_c[0] <= 0: # if player's center goes past min x-dimension of screen, they cannot go further
            self.position_c[0] = 0
        elif self.position_c[1] <= 160: # if player's center goes past min y-dimension of screen, they cannot go further
            self.position_c[1] = 160

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
        """Returns sprite collided with, of obstacle objects,
        or None if no collisions."""
        angle_bumps = {0:(-1,0), 45:(-1,1), 90:(0,1), 135:(1,1),
        180:(1,0), 225:(1,-1), 270:(0,-1), 315:(-1,-1)}

        a = self.cont.v_max      # this multiplier scales the magnitude of collision-bumping to the magnitude of the player's movement

        full_obstacle_group = Obstacle_Group('ALL_HERE')    # makes an obstacle group containing all obstacle groups
        for group in self.obstacles:
            full_obstacle_group.add(group)

        collision = pygame.sprite.spritecollide(self, full_obstacle_group, dokill = False)   # creates list of all obstacles that the player is colliding with

        if len(collision) > 0:      # if the sprite is colliding with any obstacles
            self.position_c[0] += angle_bumps[self.cont.angle][0]*a   # moves the sprite in the opposite direction of their facing
            self.position_c[1] += angle_bumps[self.cont.angle][1]*a

    def check_color_collision(self, color_objs):
        """Returns sprite collided with, of color objects,
        or None if no collisions. Keeps track of what collisions
        have already happened, and does not repeat collisions"""
        self.update_rect()

        collision = pygame.sprite.spritecollideany(self, color_objs)
        if collision:
            if collision not in self.collided_with:
                self.collided_with.append(collision)
                return collision

class Obstacle(Actor, pygame.sprite.Sprite):
    """
    Obstacle class to block off possible paths of travel
    """
    def __init__(self, cell_size, position, type, image = [pygame.image.load('./images/obstacle_spike_light.png'),pygame.image.load('./images/obstacle_spike_dark.png')]):
        """Initialize the obstacle.

        cell_size: Tuple of the dimensions of each world map cell
        position: Tuple of the coordinates of the Obstacle in pixels
        Type: Tuple of an RGB color code to correspond the obstacle
        with a certain color
        """
        super(Obstacle, self).__init__(image, cell_size, position)
        pygame.sprite.Sprite.__init__(self)

        if type[0] > 200 or type[1] > 200 or type[2] > 200:         # overlays a shadow spike layer if the obstacle color is too bright
            self.image = pygame.transform.scale(image[1], self.size)
        else:                                                       # overlays a highlight spike layer if obstacle color is dark enough
            self.image = pygame.transform.scale(image[0], self.size)

        self.type = type
        self.rect = self.image.get_rect(topleft = self.position)    # defines its own self.rect b/c it's dependent on self.image

    def __str__(self):
        return "Obstacle, type %s at location (%r)" % (self.type, self.position)

    def make_groups(self, obstacle, list):
        """Sorts obstacles into groups based off types.

        obstacle: Obstacle object of the obstacle being sorted
        list: Current list of obstacle groups

        make_groupes creates a sprite group named after each obstacle type, then adds that group to the model's obstacles list
        """
        type = obstacle.type
        if type not in list: # if there isn't already a group corresponding to this obstacle's type...
            type = Obstacle_Group(type) # ... make a group for that particular type...
            type.add(obstacle) # ... add this obstacle to that group...
            list.append(type) # ... and add this group to the model's obstacles list
        if type in list:
            type.add(obstacle) # if a corresponding group already exists, simply add this obstacle to the group

class Obstacle_Group(pygame.sprite.Group):
    """
    Makes a group to hold all obstacles of the same type
    """
    def __init__(self, type):
        pygame.sprite.Group.__init__(self)
        self.type = type

if __name__ == "__main__":
    mtn = Obstacle((50,50), (100,300), 'river',(0,0,225))
    print(mtn)

import pygame
from pygame import transform
class Darkness():
    """
    creates a black cover up to cover the screen
    """
    def __init__(self, player, screen_size,
    image = pygame.image.load('./images/flashlight6.png')):
        """
        Initialize the darkness

        player: a player object
        screen_size: a tuple of the screen dimensions
        image: image file of the darkness
        """
        self.player = player
        self.size = (int(screen_size[0]*2.5), int(screen_size[1]*2.5))

        image = transform.scale(image, self.size)
        self.image = image
        self.image_orig = image # original image to base rotation on

        # sorry this is so long, idk how to break up the line in python
        self.rotations = {0:transform.rotate(self.image_orig, 0), 45:transform.rotate(self.image_orig, 45), 90:transform.rotate(self.image_orig, 90), 135:transform.rotate(self.image_orig, 135), 180:transform.rotate(self.image_orig, 180), 225:transform.rotate(self.image_orig, 225), 270:transform.rotate(self.image_orig, 270), 315:transform.rotate(self.image_orig, 315)}
        # self.rotations is loading all of the darkness rotations, so that they can be called without causing lag

    def __str__(self):
        return "Darkness origin at location %s." % (self.player.position_c)

    def rotate(self):
        """Rotates the darkness to match the player"""
        angle = self.player.cont.angle
        self.image = self.rotations[angle]      # overlay image of darkess that points in same direction as player

    def draw_position(self):
        """Finds the draw position for the darkness based on player position"""
        player_c = self.player.position_c
        if self.player.cont.angle%90 == 0: # if on 90 degree increments
            return (player_c[0]-self.size[0]/2, player_c[1]-self.size[1]/2)
        else: # if on 45 degree increments
            a = .21
            return (player_c[0]-self.size[0]/2-self.size[0]*a, player_c[1]-self.size[1]/2-self.size[1]*a)

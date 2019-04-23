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
        self.size = (int(screen_size[0]*1.5), int(screen_size[1]*1.5))

        image = transform.scale(image, self.size)
        self.image = image
        self.image_orig = image # original image to base rotation on

    def __str__(self):
        return "Darkness origin at location %s." % (self.player.position_c)

    def rotate(self):
        """Rotates the darkness to match the player"""
        angle = self.player.cont.angle
        self.image = transform.rotate(self.image_orig, self.player.cont.angle) # rotates the image

    def draw_position(self):
        """Finds the draw position for the darkness based on player position"""
        if self.player.cont.angle%90 == 0: # if on 90 degree increments
            player_c = self.player.position_c
            return (player_c[0]-self.size[0]/2, player_c[1]-self.size[1]/2)
        else: # if on 45 degree increments
            player_c = self.player.position_c
            a = .21
            return (player_c[0]-self.size[0]/2-self.size[0]*a, player_c[1]-self.size[1]/2-self.size[1]*a)
    # fill the screen

    # angle/2 and based on facing of player

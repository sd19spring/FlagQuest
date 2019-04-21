import pygame
from pygame import transform
class Darkness():
    """
    creates a black cover up to cover the screen
    """
    def __init__(self, player, screen_size, image = pygame.image.load('./images/flashlight2.png')):
        """
        Initialize the darkness

        player: a player object
        screen_size: a tuple of the screen dimensions
        image: image file of the darkness
        """
        self.player = player
        self.screen_size = screen_size

        image = transform.scale(image, (screen_size[0]*2, screen_size[1]*2))
        self.image = image
        self.image_orig = image # original image to base rotation on
        self.draw_offset()

    def __str__(self):
        return "Darkness origin at location %s." % (self.player.position_c)

    def rotate(self):
        """Rotates the darkness to match the player"""
        angle = self.player.cont.angle
        self.image = transform.rotate(self.image_orig, self.player.cont.angle) # rotates the image

    def draw_offset(self):
        """Finds the draw offset based on the player center"""
        image_dim = self.image.get_rect().size # get the image size
        self.draw_offset = (image_dim[0]/2, image_dim[1]/2) # find the image center as an offset

    def draw_position(self):
        """Finds the draw position for the darkness based on player position"""
        pos = self.player.position_c
        return (pos[0]-self.draw_offset[0], pos[1]-self.draw_offset[1])

    # fill the screen

    # angle/2 and based on facing of player

import pygame
class Darkness():
    """
    creates a black cover up to cover the screen
    """
    def __init__(self, player, screen_size, view_angle, image = pygame.image.load('./images/flashlight.png')):
        """
        Initialize the darkness

        player: a player object
        screen_size: a tuple of the screen dimensions
        view_angle: the view angle for the player
        image: image file of the darkness
        """
        self.player = player
        self.screen_size = screen_size
        self.view_angle = view_angle
        self.image = image

    def __str__(self):
        return "Darkness origin at location %s with a %d-degree view_angle." % (self.player.position_c, self.view_angle)

    def get_draw_position(self):
        """Finds the draw position for the darkness based on player position"""
        pos = self.player.position_c
        return (pos[0]-600, pos[1]-600)


    # fill the screen

    # angle/2 and based on facing of player

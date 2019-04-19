class Darkness():
    """
    creates a black cover up to cover the screen
    """
    def __init__(self, player, screen_size, view_angle):
        """
        Initialize the darkness

        player: a player object
        screen_size: a tuple of the screen dimensions
        view_angle: the view angle for the player
        """
        self.player = player
        self.screen_size = screen_size
        self.view_angle = view_angle

    def __str__(self):
        return "Darkness origin at location %s with a %d-degree view_angle." % (self.player.position_c, self.view_angle)

    # fill the screen

    # angle/2 and based on facing of player

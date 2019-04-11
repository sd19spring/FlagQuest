import math
class Player_Controller():
    """Defines a controller that takes user input to control the Player
    object.
    """
    def __init__(self, acceleration):
        """Initialize the player controller

        acceleration: the acceleration rate of the controller"""
        self.angle = 0 # angle
        self.v_x = 0 # x velocity
        self.v_y = 0 # y velocity
        self.a = acceleration # acceleration rate of the object

    def __str__(self):
        """Print the Player_Controller info"""
        return None
        
    def accel_x(self):
        """Accelerate in the x direction
        >>> test = Player_Controller(2)
        >>> test.accel_x"""
        self.v_x += self.a

    def accel_y(self):
        """Accelerate in the y direction"""
        self.v_y += self.a

    def stop(self):
        """Stop the player from moving"""
        self.v_x = 0
        self.v_y = 0

    def facing(self):
        """Find the facing based on the current velocities"""
        self.angle = degrees(atan(self.v_x/self.v_y)) # get the facing in degrees

class Keyboard_Controller():
    """Defines a controller that takes input from the arrow keys, wasd, and ,aoe
    """
    pass

import doctest
doctest.run_docstring_examples(Player_Controller.accel_x, globals())

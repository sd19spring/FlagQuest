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
        """Print the Player_Controller info

        Added the following doctest to make sure that the method could correctly
        display the object.
        >>> print(Player_Controller(2))
        Player_Controller(angle = 0, v_x = 0, v_y = 0 acceleration = 2)"""
        return 'Player_Controller(angle = '+str(self.angle)+', v_x = '+str(self.v_x)+', v_y = '+str(self.v_y)+' acceleration = '+str(self.a)+')'

    def accel_x(self, dir):
        """Accelerate in the x direction

        Added the following doctest to make sure that accel_x could increase
        the x velocity by the acceleration value when going right.
        >>> test = Player_Controller(2)
        >>> test.accel_x('right')
        >>> print(test)
        Player_Controller(angle = 0, v_x = 2, v_y = 0 acceleration = 2)

        Added the following doctest to test going left.
        >>> test = Player_Controller(2)
        >>> test.accel_x('left')
        >>> print(test)
        Player_Controller(angle = 0, v_x = -2, v_y = 0 acceleration = 2)
        """
        if dir == 'left':
            self.v_x -= self.a
        elif dir == 'right':
            self.v_x += self.a

    def accel_y(self, dir):
        """Accelerate in the y direction

        Added the following doctest to test going up.
        >>> test = Player_Controller(2)
        >>> test.accel_y('up')
        >>> print(test)
        Player_Controller(angle = 0, v_x = 0, v_y = 2 acceleration = 2)

        Added the following doctest to test going down.
        >>> test = Player_Controller(2)
        >>> test.accel_y('down')
        >>> print(test)
        Player_Controller(angle = 0, v_x = 0, v_y = -2 acceleration = 2)"""
        if dir == 'up':
            self.v_y += self.a
        elif dir == 'down':
            self.v_y -= self.a

    def stop(self):
        """Stop the player from moving

        Added the following doctest to make sure the method could reset the
        velelocities back to zero.
        >>> test = Player_Controller(2)
        >>> test.accel_y()
        >>> test.accel_x()
        >>> test.stop()
        >>> print(test)
        Player_Controller(angle = 0, v_x = 0, v_y = 0 acceleration = 2)
        """
        self.v_x = 0
        self.v_y = 0

    def facing(self):
        """Find the facing based on the current velocities

        Added the following doctest to make sure the method could find the
        correct facing if only v_x.
        >>> test = Player_Controller(2)
        >>> test.accel_x()
        >>> test.facing()
        >>> print(test)

        Added the following doctest to make sure the method could find the
        correct facing if only v_y.

        Added the following doctest to make sure the method could find the
        correct facing if there is v_x and v_y, and the direction is in the first
        quadrant.

        Added the following doctest to test if the direction is in the second
        quadrant.

        Added the following doctest to test if the direction is in the third
        quadrant.

        Added the following doctest to test if the direction is in the fourth
        quadrant.
        """
        self.angle = degrees(atan(self.v_x/self.v_y)) # get the facing in degrees
        # way to keep track of where it is undefined
        # way to keep track of which part it is on
        # if v_x is neg, it will be facing left
        # if v_y is neg, it will be facing down

class Keyboard_Controller():
    """Defines a controller that takes input from the arrow keys, wasd, and ,aoe
    """
    pass

import doctest
doctest.run_docstring_examples(Player_Controller.stop, globals())

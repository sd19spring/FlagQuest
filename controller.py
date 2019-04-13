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
        correct facing if only v_x. Test along an axis.
        >>> test = Player_Controller(2)
        >>> test.accel_x('right')
        >>> test.facing()
        >>> print(test)
        Player_Controller(angle = 0, v_x = 2, v_y = 0 acceleration = 2)

        Added the following doctest to make sure the method could find the
        correct facing if only v_y. Test along an axis.
        >>> test = Player_Controller(2)
        >>> test.accel_y('up')
        >>> test.facing()
        >>> print(test)
        Player_Controller(angle = 90, v_x = 0, v_y = 2 acceleration = 2)

        Added the following doctest to make sure the method could find the
        correct facing if only -v_x. Test along an axis.
        >>> test = Player_Controller(2)
        >>> test.accel_x('left')
        >>> test.facing()
        >>> print(test)
        Player_Controller(angle = 180, v_x = -2, v_y = 0 acceleration = 2)

        Added the following doctest to make sure the method could find the
        correct facing if only -v_y. Test along an axis.
        >>> test = Player_Controller(2)
        >>> test.accel_y('down')
        >>> test.facing()
        >>> print(test)
        Player_Controller(angle = 270, v_x = 0, v_y = -2 acceleration = 2)

        Added the following doctest to make sure the method could find the
        correct facing if there is v_x and v_y, and the direction is in the first
        quadrant.
        >>> test = Player_Controller(2)
        >>> test.accel_y('up')
        >>> test.accel_x('right')
        >>> test.accel_x('right')
        >>> test.facing()
        >>> print(test)
        Player_Controller(angle = 26, v_x = 4, v_y = 2 acceleration = 2)

        Added the following doctest to test if the direction is in the second
        quadrant.
        >>> test = Player_Controller(2)
        >>> test.accel_y('up')
        >>> test.accel_y('up')
        >>> test.accel_x('left')
        >>> test.facing()
        >>> print(test)
        Player_Controller(angle = 117, v_x = -2, v_y = 4 acceleration = 2)

        Added the following doctest to test if the direction is in the third
        quadrant.
        >>> test = Player_Controller(2)
        >>> test.accel_y('down')
        >>> test.accel_x('left')
        >>> test.accel_x('left')
        >>> test.facing()
        >>> print(test)
        Player_Controller(angle = 206, v_x = -4, v_y = -2 acceleration = 2)

        Added the following doctest to test if the direction is in the fourth
        quadrant.
        >>> test = Player_Controller(2)
        >>> test.accel_y('down')
        >>> test.accel_y('down')
        >>> test.accel_x('right')
        >>> test.facing()
        >>> print(test)
        Player_Controller(angle = 297, v_x = 2, v_y = -4 acceleration = 2)
        """
        try:
            angle = int(math.degrees(math.atan(self.v_y/self.v_x))) # get the facing in degrees
        except ZeroDivisionError:
            angle = 0

        if self.v_x < 0: # if in quad 2 or 3
            self.angle = 180 + angle
        elif self.v_x > 0 and self.v_y < 0: # if in quandrant 4
            self.angle = 360 + angle
        elif self.v_y > 0 and self.v_x == 0: # if along the axis between quad 1 and 2
            self.angle = 90
        elif self.v_y < 0 and self.v_x == 0: # if along the axis between quad 3 and 4
            self.angle = 270
        else: # if in quandrant 1
            self.angle = angle

    # max velocity instead of acceleration
    # 45 degree facing?

class Keyboard_Controller():
    """Defines a controller that takes input from the arrow keys, wasd, and ,aoe
    """
    # rotation does
    # up arrow to move forward
    # side arrows to rotate?
    pass

import doctest
doctest.run_docstring_examples(Player_Controller.facing, globals())

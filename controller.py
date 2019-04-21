import math
import pygame
class Player_Controller():
    """Defines a controller that takes user input to control the Player
    object.
    """
    def __init__(self, max_velocity):
        """Initialize the player controller

        max_velocity: the max_velocity of the controller"""
        self.angle = 0 # angle
        self.v_x = 0 # x velocity
        self.v_y = 0 # y velocity
        self.v_max = max_velocity # acceleration rate of the object

    def __str__(self):
        """Print the Player_Controller info

        Added the following doctest to make sure that the method could correctly
        display the object.
        >>> print(Player_Controller(2))
        Player_Controller(angle = 0, v_x = 0, v_y = 0 max_velocity = 2)"""
        return 'Player_Controller(angle = '+str(self.angle)+', v_x = '+str(self.v_x)+', v_y = '+str(self.v_y)+' max_velocity = '+str(self.v_max)+')'

    def accel(self, dir):
        """Accelerate in the x direction

        Added the following doctest to make sure that accel_x could increase
        the x velocity by the acceleration value when going right.
        >>> test = Player_Controller(2)
        >>> test.accel('right')
        >>> print(test)
        Player_Controller(angle = 0, v_x = 2, v_y = 0 max_velocity = 2)

        Added the following doctest to test going left.
        >>> test = Player_Controller(2)
        >>> test.accel('left')
        >>> print(test)
        Player_Controller(angle = 0, v_x = -2, v_y = 0 max_velocity = 2)

        Added the following doctest to test going up.
        >>> test = Player_Controller(2)
        >>> test.accel('up')
        >>> print(test)
        Player_Controller(angle = 0, v_x = 0, v_y = -2 max_velocity = 2)

        Added the following doctest to test going down.
        >>> test = Player_Controller(2)
        >>> test.accel('down')
        >>> print(test)
        Player_Controller(angle = 0, v_x = 0, v_y = 2 max_velocity = 2)
        """
        if dir == 'left':
            self.v_x = -self.v_max
        elif dir == 'right':
            self.v_x = self.v_max
        if dir == 'up':
            self.v_y = -self.v_max
        elif dir == 'down':
            self.v_y = self.v_max

    def facing(self):
        """Find the facing based on the current velocities

        Added the following doctest to make sure the method could find the
        correct facing if only v_x. Test along an axis.
        >>> test = Player_Controller(2)
        >>> test.accel('right')
        >>> test.facing()
        >>> print(test)
        Player_Controller(angle = 0, v_x = 2, v_y = 0 max_velocity = 2)

        Added the following doctest to make sure the method could find the
        correct facing if only v_y. Test along an axis.
        >>> test = Player_Controller(2)
        >>> test.accel('up')
        >>> test.facing()
        >>> print(test)
        Player_Controller(angle = 90, v_x = 0, v_y = -2 max_velocity = 2)

        Added the following doctest to make sure the method could find the
        correct facing if only -v_x. Test along an axis.
        >>> test = Player_Controller(2)
        >>> test.accel('left')
        >>> test.facing()
        >>> print(test)
        Player_Controller(angle = 180, v_x = -2, v_y = 0 max_velocity = 2)

        Added the following doctest to make sure the method could find the
        correct facing if only -v_y. Test along an axis.
        >>> test = Player_Controller(2)
        >>> test.accel('down')
        >>> test.facing()
        >>> print(test)
        Player_Controller(angle = 270, v_x = 0, v_y = 2 max_velocity = 2)

        Added the following doctest to make sure the method could find the
        correct facing if there is v_x and v_y, and the direction is in the first
        quadrant.
        >>> test = Player_Controller(2)
        >>> test.accel('up')
        >>> test.accel('right')
        >>> test.facing()
        >>> print(test)
        Player_Controller(angle = 45, v_x = 2, v_y = -2 max_velocity = 2)

        Added the following doctest to test if the direction is in the second
        quadrant.
        >>> test = Player_Controller(2)
        >>> test.accel('up')
        >>> test.accel('left')
        >>> test.facing()
        >>> print(test)
        Player_Controller(angle = 135, v_x = -2, v_y = -2 max_velocity = 2)

        Added the following doctest to test if the direction is in the third
        quadrant.
        >>> test = Player_Controller(2)
        >>> test.accel('down')
        >>> test.accel('left')
        >>> test.facing()
        >>> print(test)
        Player_Controller(angle = 225, v_x = -2, v_y = 2 max_velocity = 2)

        Added the following doctest to test if the direction is in the fourth
        quadrant.
        >>> test = Player_Controller(2)
        >>> test.accel('down')
        >>> test.accel('right')
        >>> test.facing()
        >>> print(test)
        Player_Controller(angle = 315, v_x = 2, v_y = 2 max_velocity = 2)
        """
        v_y = -self.v_y
        try:
            angle = int(math.degrees(math.atan(v_y/self.v_x))) # get the facing in degrees
        except ZeroDivisionError:
            angle = 0

        if self.v_x < 0: # if in quad 2 or 3
            self.angle = 180 + angle
        elif self.v_x > 0 and v_y < 0: # if in quandrant 4
            self.angle = 360 + angle
        elif v_y > 0 and self.v_x == 0: # if along the axis between quad 1 and 2
            self.angle = 90
        elif v_y < 0 and self.v_x == 0: # if along the axis between quad 3 and 4
            self.angle = 270
        else: # if in quandrant 1
            self.angle = angle

class Keyboard_Controller(Player_Controller):
    """Defines a controller that takes input from the arrow keys, wasd, and ,aoe
    """
    def __init__(self, max_velocity):
        """Iinitialize the player controller"""
        super(Keyboard_Controller, self).__init__(max_velocity) # uses the __init__ method from Controller()
        self.move_up = [pygame.K_UP, pygame.K_w, pygame.K_COMMA]
        self.move_down = [pygame.K_DOWN, pygame.K_s, pygame.K_o]
        self.move_left = [pygame.K_LEFT, pygame.K_a]
        self.move_right = [pygame.K_RIGHT, pygame.K_d, pygame.K_e]


    def pressed (self, key):
        """Check which key is pressed"""
        if key[self.move_up[0]] == 1 or key[self.move_up[1]] == 1 or key[self.move_up[2]] == 1:
            self.accel('up')
        elif key[self.move_down[0]] == 1 or key[self.move_down[1]] == 1 or key[self.move_down[2]] == 1:
            self.accel('down')
        else:
            self.v_y = 0

        if key[self.move_left[0]] == 1 or key[self.move_left[1]] == 1 == 1:
            self.accel('left')
        elif key[self.move_right[0]] == 1 or key[self.move_right[1]] == 1 or key[self.move_right[2]] == 1:
            self.accel('right')
        else:
            self.v_x = 0

if __name__ == "__main__":
    import doctest
    doctest.testmod()

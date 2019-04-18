# http://gamingdirectional.com/blog/2016/09/03/rotate-an-object-in-pygame/
# rotated_player = pygame.transform.rotate(player, player_rotation)


import math

class Vector2D(tuple):

    def __new__(cls, x=0.0, y=0.0):
        return tuple.__new__(cls, (x, y))

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%s, %s)"%(self.x, self.y)

    @classmethod
    def next_vector(cls, args):
        return cls(args[2]-args[0], args[3]-args[1])

    def get_magnitude(self):
        return math.sqrt( self.x**2 + self.y**2 )

    def normalize(self):
        magnitude = self.get_magnitude()
        self.x /= magnitude
        self.y /= magnitude

    # rhs stands for Right Hand Side
    def __add__(self, rhs):
        return Vector2D(self.x + rhs.x, self.y + rhs.y)

    def __sub__(self, rhs):
        return Vector2D(self.x - rhs.x, self.y - rhs.y)

    def __neg__(self):
        return Vector2D(-self.x, -self.y)

    def __mul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)

    def __div__(self, scalar):
        return Vector2D(self.x / scalar, self.y / scalar)
import pygame
from pygame.locals import *
from sys import exit
# from vector2d import Vector2D
from math import *

boat = './images/player2.png'

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)
pygame.display.set_caption("Pygame Rotation Demo")

player = pygame.image.load(boat).convert_alpha()

clock = pygame.time.Clock()
player_pos = Vector2D(300, 250)

player_rotation = 0.
player_rotation_speed = 360. # 360 degrees per second

while True:

    for event in pygame.event.get():

        if event.type == QUIT:
            exit()

    pressed_keys = pygame.key.get_pressed()

    rotation_direction = 0.

    if pressed_keys[K_LEFT]:
        rotation_direction = -1.0
    if pressed_keys[K_RIGHT]:
        rotation_direction = +1.0

    screen.fill((255, 255, 255))

    rotated_player = pygame.transform.rotate(player, player_rotation) # Return the rotated_player surface object
    w, h = rotated_player.get_size()
    player_draw_pos = Vector2D(player_pos.x-w/2, player_pos.y-h/2)
    screen.blit(rotated_player, player_draw_pos)

    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0

    player_rotation += rotation_direction * player_rotation_speed * time_passed_seconds

    pygame.display.update()

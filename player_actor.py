import pygame
import time

class Player_actor(pygame.sprite.Sprite):
    """
    sprite
    position
    handle movement
    """
    def __init__(self, x_pos, y_pos, facing, filling, width, height):
        """
        initialize the player's character
        depends upon facing from controller
        filling is what the character visually looks like (for now it's just a color)
        width and height are in regards to its size and shape
        """
        pygame.sprite.Sprite.__init__(self) # set up the actor's spriteness

        self.x_pos = x_pos
        self.y_pos = y_pos
        self.v_x = 0
        self.v_y = 0
        self.facing = facing
        self.dimensions = width, height

        self.image = pygame.Surface(self.dimensions)
        self.image.fill(filling)

        self.shape = self.image.get_rect()

    def __str__(self):
        return "Player centered at location (%d, %d) with a %d-degree heading. The sprite's dimensions are %dx%d" % (self.position[0], self.position[1], self.facing, self.dimensions[0], self.dimensions[1])

    def get_keypress(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_UP] == 1:
            self.v_y = 1
            # print('up')
        if key[pygame.K_DOWN] == 1:
            self.v_y = -1
            # print('down')
        if key[pygame.K_RIGHT] == 1:
            self.v_x = 1
            # print('right')
        if key[pygame.K_LEFT] == 1:
            self.v_x = -1
            # print('left')

    def draw(self, surface):
        surface.blit(self.image, self.position)

    def move(self):
        self.x_pos += self.v_x
        self.y_pos += self.v_y
        self.position = self.x_pos, self.y_pos

if __name__ == "__main__":
    BLUE = (0, 0, 255)
    buddy = Player_actor(10,20,90,BLUE,width = 5, height = 7)

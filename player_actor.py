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
        initialize the player_actor character
        depends upon facing from controller
        filling is what the character visually looks like (for now it's just a color)
        width and height are in regards to its size and shape
        """
        pygame.sprite.Sprite.__init__(self) # set up the actor's spriteness

        self.x_pos = x_pos
        self.y_pos = y_pos
        self.v_x = 0
        self.v_y = 0
        self.facing = facing        # 4/13/19 facing has yet to be implimented
        self.dimensions = width, height

        self.image = pygame.Surface(self.dimensions)    # sets size of sprite's visual representation
        self.image.fill(filling)    # this just fills it with a color, later it will actually be an image

        # self.shape = self.image.get_rect()    # we don't need this rn (4/13/19), maybe it's important for the future though?

    def __str__(self):
        return "Player centered at location (%d, %d) with a %d-degree heading. The sprite's dimensions are %dx%d" % (self.x_pos, self.y_pos, self.facing, self.dimensions[0], self.dimensions[1])

    def get_keypress(self):
        """
        adjusts the player_actor's velocity depending on which arrowkeys are pressed
        """
        key = pygame.key.get_pressed()

        if key[pygame.K_UP] == 1:       # the up/v_y and down/v_y values seem inverted because up is down in pygame
            self.v_y = -1
        elif key[pygame.K_DOWN] == 1:
            self.v_y = 1
        else:
            self.v_y = 0

        if key[pygame.K_RIGHT] == 1:
            self.v_x = 1
        elif key[pygame.K_LEFT] == 1:
            self.v_x = -1
        else:
            self.v_x = 0

    def draw(self, screen):
        """
        blits the screen with the player_actor at its position (i.e. x_pos,y_pos)
        """
        screen.blit(self.image,self.position)   # places image of player_actor

    def move(self, step_size = 1):      # step size adjusts how many pixels the player_actor moves at a time
        self.x_pos += self.v_x*step_size
        self.y_pos += self.v_y*step_size
        self.position = self.x_pos, self.y_pos  # updates position to reflect the movement due to keyboard input

if __name__ == "__main__":
    BLUE = (0, 0, 255)
    buddy = Player_actor(10,20,90,BLUE,width = 5, height = 7)
    print(buddy)

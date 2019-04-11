import pygame

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

        self.position = x_pos, y_pos
        self.facing = facing
        self.dimensions = width, height

        self.image = pygame.Surface(self.dimensions)
        self.image.fill(filling)

        self.shape = self.image.get_rect()

    def __str__(self):
        return "Player centered at location (%d, %d) with a %d-degree heading. The sprite's dimensions are %dx%d" % (self.position[0], self.position[1], self.facing, self.dimensions[0], self.dimensions[1])

    def move(self):
        self.x_pos += controller.v_x
        self.y_pos += controller.v_y

    def update(self):
        self.move()
        # add stuff to update facing from controller

BLUE = (0, 0, 255)
buddy = Player_actor(10,20,90,BLUE,width = 5, height = 7)
print(buddy)

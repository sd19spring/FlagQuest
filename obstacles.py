import pygame

class Obstacle(pygame.sprite.Sprite):
    """
    allows you to make an obstacle to block off possible paths of travel
    """
    def __init__(self, grid_size, position, type):
        """
        grid size refers to the dimensions of each grid square on the world map
        position refers to the x,y coordinates of the Obstacle
        type refers to the group characteristics of the obstacle (s/a color)
        """
        pygame.sprite.Sprite.__init__(self)

        self.width, self.height = grid_size
        self.position = position
        self.type = type

        self.image = pygame.Surface(grid_size)    # creates a simple rectangle for the Obstacle
        self.image.fill((100,150,50))             # random green color, arbitary
        self.rect = self.image.get_rect()
        self.rect.center = (position)

    def __str__(self):
        return "Obstacle, type %s at location (%r)" % (self.type, self.position)

    def draw(self, screen):
        screen.blit(self.image, self.position)

if __name__ == "__main__":
    mtn = Obstacle((50,50), (100,300), 'purple')
    print(mtn)

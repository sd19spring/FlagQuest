import pygame

class Obstacle(pygame.sprite.Sprite):
    """
    allows you to make an obstacle to block off possible paths of travel
    """
    def __init__(self, grid_size, position, type, color):
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
        self.image.fill(color)          # color correspond's with the obstacle's "type"
        self.rect = pygame.Rect(self.position[0], self.position[1], self.width, self.height)
        self.rect.center = (position)

    # def update_rect(self):
    #     self.rect = self.image.get_rect()

    def __str__(self):
        return "Obstacle, type %s at location (%r)" % (self.type, self.position)

if __name__ == "__main__":
    mtn = Obstacle((50,50), (100,300), 'river',(0,0,225))
    print(mtn)

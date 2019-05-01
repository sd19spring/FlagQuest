import pygame

class Obstacle(pygame.sprite.Sprite):
    """
    Obstacle class to block off possible paths of travel
    """
    def __init__(self, cell_size, position, type, image = pygame.image.load('./images/obstacle.jpg')):
        """Initialize the obstacle.

        cell_size: Tuple of the dimensions of each world map cell
        position: Tuple of the coordinates of the Obstacle in pixels
        Type: Tuple of an RGB color code to correspond the obstacle
        with a certain color
        """
        pygame.sprite.Sprite.__init__(self)

        self.size = cell_size
        self.position = position
        self.type = type

        self.image = pygame.transform.scale(image, self.size)
        self.rect = pygame.Rect(self.position, self.size)

    def __str__(self):
        return "Obstacle, type %s at location (%r)" % (self.type, self.position)

    def make_groups(self, obstacle, list):
        """Sorts obstacles into groups based off types.

        obstacle: Obstacle object of the obstacle being sorted
        list: Current list of obstacle groups

        make_groupes creates a sprite group named after each obstacle type, then adds that group to the model's obstacles list
        """
        type = obstacle.type
        if type not in list: # if there isn't already a group corresponding to this obstacle's type...
            type = Obstacle_group(type) # ... make a group for that particular type...
            type.add(obstacle) # ... add this obstacle to that group...
            list.append(type) # ... and add this group to the model's obstacles list
        if type in list:
            type.add(obstacle) # if a corresponding group already exists, simply add this obstacle to the group

class Obstacle_group(pygame.sprite.Group):
    """
    makes a group to hold all obstacles of the same type
    """
    def __init__(self, type):
        pygame.sprite.Group.__init__(self)
        self.type = type

if __name__ == "__main__":
    mtn = Obstacle((50,50), (100,300), 'river',(0,0,225))
    print(mtn)

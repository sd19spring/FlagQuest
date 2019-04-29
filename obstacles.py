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

        self.image = pygame.transform.scale(pygame.image.load('./spike.jpg'), (40,40))   # creates a simple rectangle for the Obstacle
        self.rect = pygame.Rect(self.position[0], self.position[1], self.width, self.height)

    def __str__(self):
        return "Obstacle, type %s at location (%r)" % (self.type, self.position)

    def make_groups(self, obstacle, type, list):
        """
        this method is used to sort an obstacle into a group based off of its type
        make_groupes creates a sprite group named after each obstacle type, then adds that group to the model's obstacles list
        """
        if type not in list:        # if there isn't already a group corresponding to this obstacle's type...
            type = Obstacle_group(type)    # ... make a group for that particular type...
            type.add(obstacle)        # ... add this obstacle to that group...
            list.append(type)       # ... and add this group to the model's obstacles list
        if type in list:
            type.add(obstacle)        # if a corresponding group already exists, simply add this obstacle to the group

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

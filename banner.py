import pygame

class Banner():
    """

    """
    def __init__(self, name, screen_size):
        self.name = name
        self.text = pygame.image.load('./images/bannertext/' + self.name + '.png')

        self.size = (screen_size[0],160)
        self.logo = pygame.image.load('./images/FlagQuest.png')

        screen_center_x = self.size[0]/2
        screen_center_y = self.size[1]/2
        text_center_x = self.text.get_rect().size[0]/2
        text_center_y = self.text.get_rect().size[1]/2

        self.x_pos = screen_center_x - text_center_x
        self.y_pos = screen_center_y - text_center_y


        self.purple = (92,39,81)

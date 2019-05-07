import pygame

class Banner():
    """ Represents banner to fill the top portion of screen
    visual banner includes FlagQuest logo and the name of current level
    """
    def __init__(self, name, screen_size):
        self.name = name
        self.text = pygame.image.load('./images/bannertext/' + self.name + '.png')  # loads text image corresponding with flag name
        self.text = self.text.convert_alpha()

        self.size = (screen_size[0],160)
        self.logo = pygame.image.load('./images/FlagQuest.png')
        self.logo = self.logo.convert_alpha()

        self.x_pos = 0
        self.y_pos = 0

    def scale_text(self, height_desired):
        """ Adjusts scale of text image to set heigh diminsion to height_desired """
        height_original = self.text.get_rect().size[1]
        scale_value = height_desired / height_original  # gets ration between what size we want and what size the image is
        if height_original != height_desired:
            self.text = pygame.transform.rotozoom(self.text, 0, scale_value)    # rotozoom used because of how it takes scaling argument

    def scale_logo(self, height_desired):
        """ Adjusts scale of logo image to set heigh diminsion to height_desired """
        height_original = self.logo.get_rect().size[1]
        scale_value = height_desired / height_original
        if height_original != height_desired:
            self.logo = pygame.transform.rotozoom(self.logo, 0, scale_value)

    def center_text(self):
        """ Adjusts coordinates of text image to place in in horizontal center of banner """
        screen_center_x = self.size[0]/2
        screen_center_y = self.size[1]/2
        
        text_center_x = self.text.get_rect().size[0]/2
        text_center_y = self.text.get_rect().size[1]/2

        self.x_pos = screen_center_x - text_center_x
        self.y_pos = screen_center_y - text_center_y

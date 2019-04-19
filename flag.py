import pygame

class Flag:
    """Represents flag. Contains image pieces, mapped to colors, keeps track of
    colors collected to display correct flag pieces."""

    def __init__(self, name, full_image = None, image_names = None, colors = None, description = None):
        self.name = name
        self.colors = colors
        self.full_image = full_image
        self.setup_images(image_names)
        self.resize()
        self.description = description
        self.colors_up = []
        self.num_colors_up = 0
        #Change to reflect changing size of screen
        self.position = (680,20)

    def add_color(self, color = None):
        """Changes indicators so that correct flag pieces are displayed"""
        # TODO: change so that color added corresponds to color actor hit
        self.num_colors_up += 1

    def setup_images(self, image_names):
        """Loads image pieces and creates image:color dictionary"""
        self.image_pieces = [pygame.image.load(image_name) for image_name in image_names]
        self.image_piece_dict = {}
        for index in list(range(len(self.colors))):
            self.image_piece_dict[self.colors[index]] = self.image_pieces[index]

    def resize(self):
        """Resizes image pieces to 100 width, conserves aspect ratio"""
        for i in list(range(len(self.image_pieces))):
            image_piece = self.image_pieces[i]
            current_size = image_piece.get_size()
            #change to reflect changing size of screen
            image_piece = pygame.transform.scale(image_piece, (100, (int(100*current_size[1]/current_size[0]))))
            self.image_pieces[i] = image_piece

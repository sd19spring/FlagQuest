import pygame

class Flag:
    """Represents flag. Contains image pieces, mapped to colors, keeps track of
    colors collected to display correct flag pieces."""

    def __init__(self, name, image_names = None, colors = None, description = None):
        self.name = name
        self.colors = colors
        self.setup_images(image_names)
        self.description = description
        self.colors_up = []
        self.num_colors_up = 0
        #Change to reflect changing size of screen
        self.position = (1500,20)

    def add_color(self, actor = None):
        """Changes indicators so that correct flag pieces are displayed"""
        # TODO: change so that color added corresponds to color actor hit
        # self.num_colors_up += 1
        # for image in self.image_pieces:
        #     if actor.color == image_piece_dict
        image_piece = self.image_piece_dict[actor.color]
        self.colors_up.append(image_piece)

    def setup_images(self, image_names):
        """Loads image pieces and creates color:image dictionary"""
        self.image_pieces = [pygame.image.load(image_name) for image_name in image_names]

        #resize
        for i in list(range(len(self.image_pieces))):
            image_piece = self.image_pieces[i]
            current_size = image_piece.get_size()
            #change to reflect changing size of screen
            image_piece = pygame.transform.scale(image_piece, (200, (int(100*current_size[1]/current_size[0]))))
            self.image_pieces[i] = image_piece

        self.image_piece_dict = {}
        for index in list(range(len(self.colors))):
            self.image_piece_dict[self.colors[index]] = self.image_pieces[index]

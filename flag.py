import pygame

class Flag:
    """Represents flag. Contains image pieces, mapped to colors, keeps track of
    colors collected to display correct flag pieces."""

    def __init__(self, name, image_names = None, colors = None):
        self.name = name
        self.colors = colors
        self.setup_images(image_names)
        self.colors_up = []
        self.position = (1500,20)

    def add_color(self, actor = None):
        """Changes indicators so that correct flag pieces are displayed"""
        image_piece = self.image_piece_dict[actor.color]
        self.colors_up.append(image_piece)

    def setup_images(self, image_names):
        """Loads image pieces and creates color:image dictionary"""
        self.image_pieces = [pygame.image.load(image_name) for image_name in image_names]

        for i in range(len(self.image_pieces)):
            image_piece = self.image_pieces[i]
            current_size = image_piece.get_size()
            #change to reflect changing size of screen
            image_piece = pygame.transform.scale(image_piece, (200, (int(200*current_size[1]/current_size[0]))))
            self.image_pieces[i] = image_piece

        self.image_piece_dict = {}
        for index in list(range(len(self.colors))):
            self.image_piece_dict[self.colors[index]] = self.image_pieces[index]

    def complete(self):
        """Check if the flag is complete

        returns: boolean"""
        # if the number of colors up is the total number of colors
        return len(self.colors_up) == len(self.colors)

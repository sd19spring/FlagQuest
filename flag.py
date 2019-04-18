import pygame

class Flag:
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

    def add_color(self, color):
        # change so colors can be added in different orders with colors_up
        self.num_colors_up += 1

    def setup_images(self, image_names):
        self.image_pieces = [pygame.image.load(image_name) for image_name in image_names]
        self.image_piece_dict = {}
        for index in list(range(len(self.colors))):
            self.image_piece_dict[self.colors[index]] = self.image_pieces[index]

    def draw(self, screen):
        #also to change when adding colors in different order
        if self.num_colors_up:
            for i in list(range(self.num_colors_up)):
                screen.blit(self.image_pieces[i], self.position)

    def resize(self):
        for i in list(range(len(self.image_pieces))):
            image_piece = self.image_pieces[i]
            current_size = image_piece.get_size()
            print(image_piece.get_size())
            #change to reflect changing size of screen
            image_piece = pygame.transform.scale(image_piece, (100, (int(100*current_size[1]/current_size[0]))))
            print(image_piece.get_size())
            self.image_pieces[i] = image_piece

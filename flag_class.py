class Flag:
    def __init__(self, name, full_image = None, image_pieces = None, colors = None, description = None):
        self.name = name
        self.colors = colors
        self.full_image = full_image
        self.image_pieces = image_pieces
        self.image_piece_dict = {}
        for index in list(range(len(colors))):
            self.image_piece_dict[colors[index]] = self.image_pieces[index]
        self.description = description
        self.colors_up = []
        self.num_colors_up = 0
        self.position = (100,100)

    def add_color(self, color):
        # change so colors can be added in different orders with colors_up
        self.num_colors_up += 1

    def draw(self, screen):
        #also to change when adding colors in different order
        if self.num_colors_up:
            for i in list(range(self.num_colors_up)):
                screen.blit(self.image_pieces[i], self.position)

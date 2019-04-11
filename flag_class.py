class Flag:
    def __init__(self, name, full_image, image_pieces = None, colors = None, description = None):
        self.name = name
        self.colors = colors
        self.full_image = full_image
        self.image_pieces = image_pieces
        self.image_piece_dict = {}
        for index in list(range(len(colors))):
            image_piece_dict[colors[index]] = image_pieces[index]
        self.description = description

    def add_color(color):
        pass

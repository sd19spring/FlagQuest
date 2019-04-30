import pygame

class Flag:
    """Represents flag. Contains image pieces, mapped to colors, keeps track of
    colors collected to display correct flag pieces."""

    def __init__(self, name):
        """Create the flag.

        name: String of the flag name"""
        self.name = name
        self.get_colors()
        self.get_images()
        self.colors_up = []
        self.position = (1500,20)

    def get_colors(self):
        """Finds the colors for the appropriate flag in terms of
        a list of tuples containing RGB color codes."""
        self.colors = {
            "ace":[(0,0,0), (163,163,163), (255,255,255),(166,1,191)],
            "alt-lesbian":[(215,44,0),(239,116,39),(255,152,86),(255,255,255),(209,98,166),(183,85,146),(165,1,98)],
            "bi":[(215,2,112),(115,79,150),(0,56,168)],
            "intersex":[(255,216,0),(121,2,170)],
            "l-lesbian":[(184,0,144),(202,103,164),(227,118,182),(255,255,255),(243,192,221),(215,96,100),(158,40,4)],
            "nb":[(255,244,51),(255,255,255),(155,89,208),(45,45,45)],
            "pan":[(255,33,142),(255,214,0),(33,176,254)],
            "poc":[(0,0,0),(115,86,38),(233,50,34),(239,144,52),(252,228,76),(73,155,47),(23,71,173),(179,67,213)],
            "pride":[(254,0,0),(255,166,3),(255,255,0),(0,129,2),(22,20,228),(128,0,126)],
            "trans":[(13, 204, 237),(248, 183, 211),(255, 255, 255)]
            }[self.name]

    def image_paths(self):
        """Finds the image path names.

        Returns: list of strings"""
        image_paths = []
        for i in range(len(self.colors)): # run for the number of colors
            path = 'images/' + self.name + "/" + str(i+1) + ".png"
            image_paths.append(path)
        return image_paths

    def get_images(self):
        """Loads images for the flag into a dictionary
        to associate the approapriate color with the
        appropriate image"""
        image_paths = self.image_paths() # get the image path
        # load the appropriate image for each image name
        images = [pygame.image.load(image_name) for image_name in image_paths]

        self.images_dict = {}
        # run for the number of colors on the flag
        for i in range(len(self.colors)):
            self.images_dict[self.colors[i]] = images[i]

    def add_color(self, actor = None):
        """Adds the appropriate image to the colors_up list."""
        image = self.images_dict[actor.color]
        self.colors_up.append(image)

    def complete(self):
        """Check if the flag is complete.

        returns: boolean"""
        # if the number of colors up is the total number of colors
        return len(self.colors_up) == len(self.colors)

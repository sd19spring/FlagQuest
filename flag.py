import pygame
import os

class Flag:
    """Represents flag. Contains image pieces, mapped to colors, keeps track of
    colors collected to display correct flag pieces."""

    def __init__(self, name,):
        self.name = name
        self.get_colors()
        self.get_images()
        self.colors_up = []
        self.position = (1500,20)

    def get_colors(self):
        all_flag_dict = {"ace":[(0,0,0), (163,163,163), (255,255,255),(166,1,191)],
                    "alt-lesbian":[(215,44,0),(239,116,39),(255,152,86),(255,255,255),(209,98,166),(183,85,146),(165,1,98)],
                    "bi":[(215,2,112),(115,79,150),(0,56,168)],
                    "intersex":[(255,216,0),(121,2,170)],
                    "l-lesbian":[(184,0,144),(202,103,164),(227,118,182),(255,255,255),(243,192,221),(215,96,100),(158,40,4)],
                    "nb":[(255,244,51),(255,255,255),(155,89,208),(45,45,45)],
                    "pan":[(255,33,142),(255,214,0),(33,176,254)],
                    "poc":[(0,0,0),(115,86,38),(233,50,34),(239,144,52),(252,228,76),(73,155,47),(23,71,173),(179,67,213)],
                    "pride":[(254,0,0),(255,166,3),(255,255,0),(0,129,2),(22,20,228),(128,0,126)],
                    "trans":[(13, 204, 237),(248, 183, 211),(255, 255, 255)]}
        self.colors = all_flag_dict[self.name]

    def image_paths(self):
        dir = os.path.dirname(os.path.realpath(__file__)) # find the current folder
        image_paths = []
        for i in range(len(self.colors)): # run for the number of colors
            path = dir + '/images/' + self.name + "/" + str(i+1) + ".png"
            image_paths.append(path)
        return image_paths

    def get_images(self):
        """Loads image pieces and creates color:image dictionary"""
        image_paths = self.image_paths()
        self.image_pieces = [pygame.image.load(image_name) for image_name in image_paths]

        for i in range(len(self.image_pieces)):
            image_piece = self.image_pieces[i]
            current_size = image_piece.get_size()
            #change to reflect changing size of screen
            image_piece = pygame.transform.scale(image_piece, (200, (int(200*current_size[1]/current_size[0]))))
            self.image_pieces[i] = image_piece

        self.image_piece_dict = {}
        for index in list(range(len(self.colors))):
            self.image_piece_dict[self.colors[index]] = self.image_pieces[index]

    def add_color(self, actor = None):
        """Changes indicators so that correct flag pieces are displayed"""
        image_piece = self.image_piece_dict[actor.color]
        self.colors_up.append(image_piece)

    def complete(self):
        """Check if the flag is complete

        returns: boolean"""
        # if the number of colors up is the total number of colors
        return len(self.colors_up) == len(self.colors)

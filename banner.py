import pygame

class Banner():

    def __init__(self, name, colors, size = (1880,160)):
        self.name = name
        self.colors = colors

        self.titles = {
            "ace":'ASEXUAL PRIDE FLAG',
            "alt-lesbian":'LESBIAN PRIDE FLAG ver.2018',
            "bi":'BISEXUAL PRIDE FLAG',
            "intersex":'INTERSEX PRIDE FLAG',
            "l-lesbian":'LESBIAN PRIDE FLAG ver.LIPSTICK',
            "nb":'NONBINARY PRIDE FLAG',
            "pan":'PANSEXUAL PRIDE FLAG',
            "poc":'PHILIDELPHIA PRIDE FLAG',
            "pride":'RAINBOW PRIDE FLAG',
            "trans":'TRANSGENDER PRIDE FLAG',
            "gqueer":'GENDERQUEER PRIDE FLAG'
            }

        self.purple = (10, 94, 200)
        self.size = size

        self.piece_mask = pygame.image.load('./images/flag_piece_mask.png')

    def make_rectangle(self):
        """ Return the banner's outline and background """
        border = Rect(0, 0, self.size[0], self.size[1])
        box = Rect(10, 10, self.size[0]-20, self.size[1]-20)
        return pygame.draw.rect(border, (0,0,0), box, width=0)

    def make_type(self):
        """ Return text object for the banner's text """
        pygame.font.init()
        font_size = 5
        font = pygame.font.Font("./fonts.RAILWAY.OTF", font_size)
        text = self.titles[name]
        while font.size(text)[1] < 100:
            font_size +=2
            font = pygame.font.Font("./fonts.RAILWAY.OTF", font_size)
        text = font.render(text, True, (255,255,255), background=None)
        return text

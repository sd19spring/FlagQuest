import pygame
import gameworld

class Banner():

    def __init__(self, name, colors, screen, screen_size):
        self.name = name
        self.colors = colors
        self.screen = screen

        self.size = (screen_size[0],160)
        self.logo = pygame.image.load('./images/FlagQuest.png')

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

        self.purple = (92,39,81)

    def draw_rectangle(self):
        """ Return the banner's outline and background """
        box = pygame.Rect(0, 0, self.size[0], self.size[1])
        pygame.draw.rect(self.screen, (0,0,0), box)     # draws black rectangle as background for banner contents

    def draw_logo(self):
        """ places FlagQuest logo at top-left corner of make_rectangle box """
        self.screen.blit(self.logo, (10,10))

    def draw_type(self):
        """ Return text object for the banner's text """
        pygame.font.init()
        font_size = 5
        font = pygame.font.Font("./fonts.RAILWAY.OTF", font_size)
        text = self.titles[name]
        while font.size(text)[1] < 100:
            font_size +=2
            font = pygame.font.Font("./fonts.RAILWAY.OTF", font_size)
        text = font.render(text, True, (255,255,255), background=None)

    def make_banner(self):
        self.draw_rectangle()
        self.draw_logo()
        # self.draw_type()

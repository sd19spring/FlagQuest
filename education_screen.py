import pygame

class Page():
    def __init__(self, image_loc, size, page_number):
        self.image = pygame.transform.scale(pygame.image.load(image_loc), size)
        self.page_number = page_number

class Book():
    def __init__(self, flag_name, size):
        """
        flag_name: string of the flag name
        size: tuple of the book dimensions
        """
        self.flag = flag_name
        self.screen = screen_size
        self._init_pages()

    def _init_pages(self):
        """Get the pages for the book"""
        self.page_n = 1 # current page
        self.pages = [] # list of the pages
        while searching:
            try:

            except SOMETHING:
                searching = False
            self.pages.append(page_n)

    def flip_page(self, direction)
        if direction == 'left' and page_n > 0

        elif direction == 'right':

class EndScreen():
    def __init__(self, flag_name, screen_size):
        pass
    def get_keypress(self):
        self.cont.pressed(pygame.key.get_pressed())

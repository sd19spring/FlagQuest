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
        self.size = size
        self.get_pages()
        self.current_page = 0

    def get_pages(self):
        """Get the pages for the book

        returns: list of the pages"""
        self.pages = [] # list of the pages

        n = 0 # current page
        searching = True
        while searching:
            try:
                page = Page('./images/books/' + self.flag + '/' + str(n) + '.png', self.size, n)
            except pygame.error: # if reached the end
                searching = False
            self.pages.append(page)
            n += 1 # advance to next page

    def flip_page(self, direction):
        """Flip the page in the book if there is another page in that direction"""
        # if flipping left and not on the first page
        if direction == 'left' and self.current_page > 0:
            self.current_page += -1
        # if flipping right and not on the last page
        elif direction == 'right' and self.current_page < (len(self.pages)-1):
            self.current_page += 1

class EndScreen():
    def __init__(self, flag_name, screen_size):
        self.flag = flag_name
        self.screen_size = screen_size
        self.book = Book(self.flag, self.screen_size) # create a book to fill the screen

    def pressed(self, key):
        self.move_left = [pygame.K_LEFT, pygame.K_a]
        self.move_right = [pygame.K_RIGHT, pygame.K_d, pygame.K_e]
        if key in self.move_left:
            self.book.flip_page('left')
        if key in self.move_right:
            self.book.flip_page('right')
        # if key[self.move_left[0]] == 1 or key[self.move_left[1]] == 1 == 1:
        #     self.book.flip_page('left')
        # elif key[self.move_right[0]] == 1 or key[self.move_right[1]] == 1 or key[self.move_right[2]] == 1:
        #     self.book.flip_page('right')

if __name__ == '__main__':
    EndScreen('trans', (1920, 1080))

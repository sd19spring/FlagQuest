import image
from flag import *
from PIL import Image, ImageDraw

class FinalScreen():
    """
    The screen that appears at the end of the game
    """
    def __init__(self, screen_size, flag_name):
        """Initialize the screen with the necessary info.
        screen_size: A tuple with the screen dimensions.
        flag_name: The name of the flag in question."""
        self.screen_size = screen_size
        self.flag = flag_name # contains the colors, image, and name
        self.get_text()

    def __str__(self):
        return "Final screen for the %s flag of size %s." % (self.flag, self.screen_size)

    def scale_image(self):
        """Scale the flag image to fit into the top 1/4 of the window"""
        pass

    def get_text(self):
        """Pull the text out of the flag info txt file"""
        f = open('./flag_info/' + self.flag + '.txt', 'r') # opens the file in read mode
        lines = f.readlines()
        self.title = lines[0]
        self.description = lines[1]
        self.colors = lines[2]
        self.history = lines[3]
        print(self.title)
        print(self.description)
        print(self.colors)
        print(self.history)
        # remove spaces in the name

    def draw (self):
        """Draw the final screen"""
        img = Image.new('RGB', (100, 30), color = (73, 109, 137))
        # d = ImageDraw.Draw('./images/trans/1.png')
        d = ImageDraw.Draw(img)
        d.show()
        # images
        # text
        # background color

if __name__ == "__main__":
    screen_size = (800, 800)
    final = FinalScreen(screen_size, 'format')
    print(final)
    final.draw()

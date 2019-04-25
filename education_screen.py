from flag import *
import PIL
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

    def get_text(self):
        """Pull the text out of the flag info txt file"""
        filename = './flag_info/' + self.flag + '.txt'
        with open(filename) as f:
            lines = f.read().splitlines()
        self.title = lines[0]
        self.description = lines[1]
        self.colors = lines[2]
        self.history = lines[3]
        # remove spaces in the name?

    def scale_image(self):
        """Scale the flag image to fit into the top 1/4 of the window"""
        pass

    def draw_background(self):
        self.img = Image.new('RGBA', self.screen_size, color = (255, 255, 255)) # create background

    def make_flag(self):
        stripe = Image.open('./images/'+ self.flag + '/1.png') # get the first stripe
        self.flag_img = Image.new("RGBA", stripe.size) # make the flag the right dimensions

        running = True
        n = 2
        while running == True:
            self.flag_img = Image.alpha_composite(self.flag_img, stripe)
            try:
                stripe = Image.open('./images/'+ self.flag + '/' + str(n) + '.png')
            except FileNotFoundError:
                running = Flase
            n += 1

    def center(self, text, coord):
        """Center the text around the given coord.

        text: string of text to center
        coord: tuple of the text center coordinates"""
        draw = ImageDraw.Draw(self.img)
        w, h = draw.textsize(text) # get the size of the text given the text size of the image
        W, H = coord
        return ((W-w)/2,(H-h)/2)

    def draw (self):
        """Draw the final screen"""
        self.draw_background()
        # self.img.textsize = 12

        title = ImageDraw.Draw(self.img)
        position = self.center(self.title, (self.screen_size[0], 30))
        title.text(position, self.title, fill=(0,0,0))
        self.img.save('./flag_info/' + self.flag + '_final.png')

        # text.text((1*self.screen_size[0]/2,10), self.text.title, fill=(0,0,0))
        # enter(self.text.title, (1*self.screen_size[0]/2,10))
        # flag = Image.open('./images/'+ self.flag + '/1.png')
        # self.make_flag()
        # img.paste(self.flag_img)

        # images
        # text
        # background color

if __name__ == "__main__":
    screen_size = (1200, 800)
    final = FinalScreen(screen_size, 'format')
    print(final)
    final.draw()

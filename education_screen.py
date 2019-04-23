from flag import *
import os

class FinalScreen():
    """
    The screen that appears at the end of the game
    """
    def __init__(self, screen_size, flag):
        """Initialize the screen with the necessary info.
        screen_size: A tuple with the screen dimensions.
        flag: The name of the flag in question."""
        self.screen_size = screen_size
        self.flag = flag # contains the colors, image, and name

    def __str__(self):
        return "Final screen for the %s of size %s." % (self.flag.name, self.screen_size)

if __name__ == "__main__":
    screen_size = (800, 800)

    dir_path = os.path.dirname(os.path.realpath(__file__))      # dir_path allows us to refer to the current folder of this file
    trans = {
            'colors' : [(13, 204, 237), (248, 183, 211), (255, 255, 255)],
            'name' : 'Trans Pride Flag',
            'description': 'This is the trans flag',
            'img_names':[dir_path + '/images/trans/t_blue.png', dir_path + '/images/trans/t_pink.png', dir_path + '/images/trans/t_white.png']  # these paths are dependent on the current locations of the image files, and should be adjusted to allow for variability in the coder's set-up
    }
    f_dict = trans
    flag = Flag(f_dict['name'], image_names = f_dict['img_names'],
                        colors = f_dict['colors'], description = f_dict['description'])
    final = FinalScreen(screen_size, flag)
    print(final)

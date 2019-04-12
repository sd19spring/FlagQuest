import pygame

class View():
    def __init__(self, width, height, filling):
        self.screen = pygame.display.set_mode((width, height))  # sets screen dimensions
        self.screen.fill(filling)        # sets background color
        pygame.display.set_caption('Window Viewer')             # sets window caption
        pygame.display.flip()            # updates contents of entire display

color = (144, 238, 144, 1)               # a painfully bright tone of green
window = View(700,500,color)

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

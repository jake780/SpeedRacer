import pygame

from racer import Racer
from street import Street

background = pygame.image.load("assets/grass.png")

class Game():
    def __init__(self):

        # Create Racer
        self.game_width = 800
        self.game_height = 600

        self.racer = Racer(self)
        self.street = Street(self)
        self.window = pygame.display.set_mode((self.game_width,self.game_height))
        self.window.blit(background, (0,0))

    def draw(self):
        self.street.draw()
        self.racer.draw()

    def move(self, keys):
        self.racer.move(keys)
    
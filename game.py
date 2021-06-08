import pygame

from racer import Racer
from street import Street

class Game():
    def __init__(self):
        # Define Game size
        self.game_width = 800
        self.game_height = 600

        # Create Game objects
        self.racer = Racer(self)
        self.street = Street(self)

        # Create pygame surface
        self.window = pygame.display.set_mode((self.game_width,self.game_height))

        # Game Speed
        self.game_speed = 1

    def draw(self):
        """Draw Game objects"""
        self.street.draw()
        self.racer.draw()

    def move(self, keys):
        """Move Game Objects"""
        self.racer.move(keys)
    
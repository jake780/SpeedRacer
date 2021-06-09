import pygame

from racer import Racer
from street import Street

class Game():
    def __init__(self):
        # Define Game size
        self.width = 800
        self.height = 600

        # Create Game objects
        self.racer = Racer(self)
        self.street = Street(self)

        # Create pygame surface
        self.background = pygame.image.load("assets/grass.png")
        self.window = pygame.display.set_mode((self.width,self.height))
        self.window.blit(self.background, (0,0))

        # Game Speed
        self.speed = 2

        # Player Score
        self.score = 0

    def draw(self):
        """Draw Game objects"""
        self.street.draw()
        self.racer.draw()

    def move(self, keys):
        """Move Game Objects"""
        self.racer.move(keys)
    
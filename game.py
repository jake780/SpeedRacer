import pygame
import random

from racer import Racer
from street import Street
from scoreboard import Scoreboard

class Game():
    def __init__(self):
        # Define Game size
        self.width = 800
        self.height = 600

        # Create pygame surface
        self.draw_background()

        # Create Game objects
        self.racer = Racer(self)
        self.street = Street(self)
        self.scoreboard = Scoreboard(self)

        # Game Speed
        self.speed = 2

        # Player Score
        self.score = 0

        self.difficulty = 50

    def add_traffic(self):
        num = random.randint(0,self.difficulty)
        if num == self.difficulty % 2:
            self.street.add_car()

    def draw_background(self):
        self.background = pygame.image.load("assets/grass.png")
        self.window = pygame.display.set_mode((self.width,self.height))
        self.window.blit(self.background, (0,0))

    def draw(self):
        """Draw Game objects"""
        self.street.draw()
        self.racer.draw()

    def move(self, keys):
        """Move Game Objects"""
        self.racer.move(keys)
        
    
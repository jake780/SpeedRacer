import pygame
import random

from racer import Racer
from street import Street
from scoreboard import Scoreboard

# Delete later, for testing
from time import sleep

class Game():
    """Controls the game"""
    def __init__(self):
        # Mainloop Variable
        self.isRunning = False

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

        self.difficulty = 100

    def add_traffic(self):
        """Adds car obstacles to the game"""
        num = random.randint(0,self.difficulty)
        if num == self.difficulty % 2:
            self.street.add_car()

    def draw_background(self):
        """Displays the game background"""
        self.background = pygame.image.load("assets/grass.png")
        self.window = pygame.display.set_mode((self.width,self.height))
        self.window.blit(self.background, (0,0))

    def title_screen(self):
        """Displays the Title screen"""
        self.scoreboard.show_logo()
        self.scoreboard.show_start_message()

    def draw(self):
        """Draw Game objects"""
        self.street.draw()
        self.racer.draw()

    def move(self, keys):
        """Move Game Objects"""
        self.racer.move(keys)

    def collide(self):
        """Game Collisions"""
        for obstacle in self.street.obstacles:
            if self.racer.collide(obstacle):
                self.end()

    def end(self):
        """End the current Game"""
        print("Game OVER!!!")
        print("Score: NA")

        self.scoreboard.show_game_over_message()
        sleep(5)
        self.isRunning = False

        
    def run(self, keys):
        """Runs all needed game methods"""
        self.add_traffic()
        self.collide()
        self.move(keys)
        self.draw()
    
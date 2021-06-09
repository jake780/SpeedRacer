import pygame
import random

class Obstacle():
    """Parent Class"""
    def __init__(self, game):
        self.game = game
        self.x = self.random_start()
        self.y = 0
        self.color = (255,0,0)
        self.width = 20
        self.height = 50

    def random_start(self):
        return random.randint(self.game.street.x, self.game.street.x + self.game.street.width)
        
    def move(self):
        """Advance Obstacle down street"""
        if self.y > self.game.height:
            self.game.street.obstacles.remove(self)
            self.game.score += 1
        else:
            self.y += self.game.speed
    
    @property
    def draw(self):
        """Draw the Obstacle"""
        pass

    def collide(self):
        """Collision Checking"""
        pass

class Car(Obstacle):
    """Traffic"""
    def __init__(self, game):
        super().__init__(game)
        self.color = (0,200,200)
        self.width = 40
        self.height = 60

    def draw(self):
        pygame.draw.rect(self.game.window, self.color, (self.x, self.y, self.width, self.height))

class Bus(Obstacle):
    """Traffic"""
    def __init__(self):
        pass

class Pedestrian(Obstacle):
    """Traffic"""
    def __init__(self):
        pass

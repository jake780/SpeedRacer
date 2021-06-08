import pygame

class Racer():
    def __init__(self, game):
        self.game = game
        self.x = self.game.game_width // 2
        self.y = self.game.game_width // 2
        self.width = 30
        self.height = 50

        self.x_vel = 0
        self.y_vel = 0
        self.speed = 0.6
        self.brakes = .9

        self.color = (255,255,255)

    def draw(self):
        pygame.draw.rect(self.game.window, self.color, (self.x, self.y, self.width, self.height))

    def move(self, keys):
        #Velocity of the car, when moving
        self.x += self.x_vel
        self.y += self.y_vel
        
        #Slow me Down
        self.x_vel *= self.brakes
        self.y_vel *= self.brakes

        #Bounderies of the Vehicle
        #Left
        if self.x < (self.game.street.x + self.game.street.sidewalk_width):
            self.x = self.game.street.x + self.game.street.sidewalk_width
        #Right
        if self.x > ((self.game.street.x + self.game.street.width) - self.game.street.sidewalk_width - self.width):
            self.x = ((self.game.street.x + self.game.street.width) - self.game.street.sidewalk_width - self.width)
        #Top
        if self.y < 0:
            self.y = 0
        #Bottom
        if self.y > self.game.game_height - self.height:
            self.y = self.game.game_height - self.height

        #Movements
        if keys[275]:
            #Right
            self.x_vel += self.speed
        if keys[276]:
            #Left
            self.x_vel -= self.speed
        if keys[274]:
            #Down
            self.y_vel += self.speed
        if keys[273]:
            #Up
            self.y_vel -= self.speed


import pygame

car_image = pygame.image.load("assets/cars/Car.png")

class Racer():
    """Player Car"""
    def __init__(self, game):
        self.game = game
        self.width = 100
        self.height = 100
        self.x = (self.game.width // 2) - (self.width//2)
        self.y = self.game.height - (self.game.height // 8)

        self.x_vel = 0
        self.y_vel = 0
        self.speed = 0.25
        self.brakes = .925

        self.color = (249, 1, 91)
        self.tire_color = (146, 148, 158)

        #This is for future car selection
        self.car_images = [""]

        self.car = car_image
        self.car = pygame.transform.scale(self.car, (self.width, self.height))

    def draw(self):
        self.game.window.blit(self.car, (self.x, self.y, self.width, self.height))

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
        if self.y > self.game.height - self.height:
            self.y = self.game.height - self.height

        #Movements
        #Right
        if keys[100]:
            self.x_vel += self.speed
        #Left
        if keys[97]:
            self.x_vel -= self.speed
        #Down
        if keys[115]:
            self.y_vel += self.speed
        #Up
        if keys[119]:
            self.y_vel -= self.speed


import pygame

class Racer():
    """Player Car"""
    def __init__(self, game):
        self.game = game
        self.width = 100
        self.height = 100

        self.hitbox_width = 35
        self.hitbox_height = 100

        self.x = (self.game.width // 2) - (self.width//2)
        self.y = self.game.height - (self.game.height // 8)

        self.x_vel = 0
        self.y_vel = 0
        self.speed = 0.25
        self.brakes = .925

        self.color = (249, 1, 91)
        self.tire_color = (146, 148, 158)

        self.racer_image = pygame.image.load("assets/cars/Car.png")

        #This is for future car selection
        self.car_images = [""]

        self.car = self.racer_image
        self.car = pygame.transform.scale(self.car, (self.width, self.height))

    def collide(self, object):
        """Returns True if the Racer collides with object"""
        # If x Collide and y Collide
        if ((self.x + self.hitbox_width > object.x) and (self.x < (object.x + object.width//3))) and ((self.y + self.hitbox_height > object.y) and (self.y < (object.y + object.height))):
            return True
        else:
            return False

    def draw(self):
        """Draw the Racer"""
        self.game.window.blit(self.car, (self.x, self.y, self.width, self.height))

        # Test draw hitbox
        pygame.draw.rect(self.game.window, self.color, (self.x + self.width //3, self.y, self.hitbox_width, self.hitbox_height))
        

    def move(self, keys):
        """Move the Racer"""
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


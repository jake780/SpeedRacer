import pygame

from obstacles import Car

class Line():
    def __init__(self, street):
        self.street = street
        self.width = 8
        self.height = self.street.line_height
        self.x  = 400
        self.y = -self.height
        self.color = (250, 250, 0)

    def move(self):
        if self.y > self.street.game.height:
            self.street.lines.remove(self)
        else:
            self.y += self.street.game.speed

    def draw(self):
        pygame.draw.rect(self.street.game.window, self.color, (self.x, self.y, self.width, self.height))


class Street():
    """Game Surface"""
    def __init__(self, game):
        self.game = game

        self.width = 600
        self.height = self.game.height

        self.x = (self.game.width //  2) - (self.width // 2)
        self.y = 0

        self.sidewalk_width = 35
        self.street_color = (0,0,0)
        self.sidewalk_color = (203, 188, 188)

        self.line_height = 50
        self.lines = []
        self.last_line = 0

        self.obstacles = []

    def sidewalks(self):
        pygame.draw.rect(self.game.window, self.sidewalk_color, (self.x, self.y, self.sidewalk_width, self.height))
        pygame.draw.rect(self.game.window, self.sidewalk_color, (self.x + self.width - self.sidewalk_width, self.y, self.sidewalk_width, self.height))

    def add_line(self):
        if self.last_line > self.line_height * 2:
            self.last_line = 0
            self.lines.append(Line(self))
        else:
            self.last_line += self.game.speed

    def add_car(self):
        """testing"""
        self.obstacles.append(Car(self.game))

    def move_road(self):
        # Lines
        for line in self.lines:
            line.move()
            line.draw()
        self.add_line()

        # Obstacles
        for ob in self.obstacles:
            ob.move()
            ob.draw()

    def draw(self):
        #Drawing Street
        pygame.draw.rect(self.game.window, self.street_color, (self.x, self.y, self.width, self.height))
        # Drawing Sidewalks
        self.sidewalks()
        # Advancing and Drawing Road and Obstacles
        self.move_road()

      

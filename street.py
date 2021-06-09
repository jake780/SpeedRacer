import pygame

class Line():
    def __init__(self, street):
        self.street = street
        self.width = 8
        self.height = 50
        self.x  = 400
        self.y = (0-self.height)
        self.color = (250, 250, 0)

    def move(self):
        if self.y > self.street.game.height:
            self.street.lines.remove(self)
            self.street.lines.append(Line(self.street))
        else:
            self.y += 1

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

        self.lines = []
        for _ in range(8):
            self.lines.append(Line(self))

    def sidewalks(self):
        pygame.draw.rect(self.game.window, self.sidewalk_color, (self.x, self.y, self.sidewalk_width, self.height))
        pygame.draw.rect(self.game.window, self.sidewalk_color, (self.x + self.width - self.sidewalk_width, self.y, self.sidewalk_width, self.height))

    def move_road(self):
        for line in self.lines:
            line.move()
            line.draw()

        

    def draw(self):
        #Drawing Street
        pygame.draw.rect(self.game.window, self.street_color, (self.x, self.y, self.width, self.height))
        self.sidewalks()
        self.move_road()

      

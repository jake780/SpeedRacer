import pygame

class Street():
    def __init__(self, game):
        self.game = game

        self.width = 600
        self.height = self.game.game_height

        self.x = (self.game.game_width //  2) - (self.width // 2)
        self.y = 0

        self.sidewalk_width = 35

        self.street_color = (0,0,0)
        self.sidewalk_color = (203, 188, 188)
        self.line_color = (250, 250, 0)

    def sidewalks(self):
        pygame.draw.rect(self.game.window, self.sidewalk_color, (self.x, self.y, self.sidewalk_width, self.height))
        pygame.draw.rect(self.game.window, self.sidewalk_color, (self.x + self.width - self.sidewalk_width, self.y, self.sidewalk_width, self.height))

    def lines(self):
        spacing = 10
        for x in range(8):
            pygame.draw.rect(self.game.window, self.line_color, (((self.game.game_width // 2) - 5), spacing * 2, 8, 50))
            spacing = spacing + 50
        

    def draw(self):
        #Drawing Streeeeet
        pygame.draw.rect(self.game.window, self.street_color, (self.x, self.y, self.width, self.height))
        self.sidewalks()
        self.lines()
      

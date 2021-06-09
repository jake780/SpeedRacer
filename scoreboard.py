import pygame

class Scoreboard():
    def __init__(self, game):
        self.game = game

        pygame.font.init()
        self.game_font = pygame.font.SysFont("Comic Sans", 20)
        self.text_color = (255,255,255)

        self.start_message = self.game_font.render('Eat Ass Smoke Grass', False, self.text_color)

    def show_start_message(self):
        """Eat ass smoke grass"""
        self.game.window.blit(self.start_message, (200,200))
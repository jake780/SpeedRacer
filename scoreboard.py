import pygame

class Scoreboard():
    def __init__(self, game):
        self.game = game

        pygame.font.init()
        self.start_font = pygame.font.SysFont("Comic Sans", 50)
        self.logo_font = pygame.font.SysFont("Arial", 140, True)
        self.logo_font.set_underline(True)
        self.start_color = (0, 18, 25)
        self.logo_color = (233, 216, 166)

        # Start message
        self.start_message = self.start_font.render("Press [SPACE] to Race!", False, self.start_color)
        self.start_message_width = self.start_message.get_rect().width
        self.start_message_height = self.start_message.get_rect().height

        # Logo
        self.logo = self.logo_font.render("SpeedRacer", False, self.logo_color)
        self.logo_width = self.logo.get_rect().width
        self.logo_height = self.logo.get_rect().height
        self.logo_image = pygame.image.load('assets/logo.gif')
        self.logo_image = pygame.transform.scale(self.logo_image, (self.width, self.height))
        

    def show_start_message(self):
        """Eat ass smoke grass"""
        self.game.window.blit(self.start_message, ((self.game.width // 2) - (self.start_message_width // 2), self.game.height - self.start_message_width))
        
    def show_logo(self):
        self.game.window.blit(self.logo, ((self.game.width // 2) - (self.logo_width // 2), 0))
        self.game.window.blit(self.logo_image, ((self.game.width // 2) - (self.logo_width // 2 + 50), 0))

import pygame

from game import Game
from racer import Racer

framerate = 10
game = Game()


def main():
    isRunning = True
    isStarted = False
    while isRunning:
        pygame.time.delay(framerate)
        pygame.event.pump()
        pygame.display.update()

        keys = pygame.key.get_pressed()

        
        # Start message
        if keys[32] and not isStarted:
            isStarted = True
        if isStarted:
            game.move(keys)
            game.draw()
        else:
            game.scoreboard.show_logo()
            game.scoreboard.show_start_message()

        if keys[27]:
            print("Gamed Closed via ESC")
            isRunning = False
            pygame.quit()


if __name__ == "__main__":
    main()
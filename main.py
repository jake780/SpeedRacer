"""Speed Racer Version 1.0"""

import pygame

from game import Game
from racer import Racer

framerate = 10
game = Game()

def main():
    """SpeedRacer Main Loop"""

    # Loop Variable
    isRunning = True
    # Game Started Variable
    isStarted = False

    # Main Loop
    while isRunning:
        pygame.time.delay(framerate)
        pygame.event.pump()
        pygame.display.update()

        # Key Press Dictionary
        keys = pygame.key.get_pressed()

        # Press Space to start the Game
        if keys[32] and not isStarted:
            isStarted = True
            game.draw_background()
        # Game running
        if isStarted:
            game.run(keys)
        # Game start Screen
        else:
            game.title_screen()

        # Quit
        if keys[27]:
            print("Gamed Closed via ESC")
            isRunning = False
            pygame.quit()


if __name__ == "__main__":
    main()
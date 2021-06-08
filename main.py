import pygame

from game import Game
from racer import Racer

framerate = 10

game = Game()

def main():
    isRunning = True
    while isRunning:

        game.draw()

        pygame.time.delay(framerate)
        pygame.event.pump()
        pygame.display.update()

        game.window.fill((0,80,0))

        keys = pygame.key.get_pressed()
        game.move(keys)

        if keys[27]:
            print("Gamed Closed via ESC")
            isRunning = False
            pygame.quit()


if __name__ == "__main__":
    main()
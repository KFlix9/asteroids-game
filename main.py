import pygame as pg
from pygame.locals import *
from constants import *


def main():
    pg.init()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        screen.fill('#BF616A')
        # screen.fill('#BF616A') you can give this any color code
        pg.display.flip()


if __name__ == "__main__":
    main()
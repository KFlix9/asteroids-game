import pygame as pg
from pygame.locals import *
from constants import *


def main():
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pg.time.Clock()
    dt = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        screen.fill('black')
        pg.display.flip()

        # limit FPS rate
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
import pygame as pg
from pygame.locals import *
from constants import *
from player import *


def main():
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pg.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) 
    dt = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        screen.fill('black')
        player.update(dt)    #turn
        player.draw(screen)
        pg.display.flip()

        # limit FPS rate, we don't need the delta (dt) for now
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
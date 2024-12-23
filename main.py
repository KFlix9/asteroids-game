import sys 
import pygame as pg

from pygame.locals import *
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *


def main():
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pg.time.Clock()

    updatable = pg.sprite.Group()
    drawable = pg.sprite.Group()
    asteroids = pg.sprite.Group()
    shots = pg.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable) 
    AsteroidField.containers = updatable
    asteroidfield = AsteroidField() 
    Shot.containers = (shots, updatable, drawable) 

    self.containers = (updatable, drawable) 
    player = self(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) 

    dt = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        for entity in updatable:
            entity.update(dt)

        for asteroid in asteroids:
            if asteroid.does_collide(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.does_collide(shot):
                    asteroid.split()
                    shot.kill()

        screen.fill('black')

        for entity in drawable:
            entity.draw(screen)

        pg.display.flip()

        # limit FPS rate, we don't need the delta (dt) for now
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
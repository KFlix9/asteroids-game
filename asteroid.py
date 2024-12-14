import pygame as pg

class Asteroid(Circleshape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pg.draw.circle(screen, "white", (self.x, self.y), self.radius)
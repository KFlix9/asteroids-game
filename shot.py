import pygame as pg

from circleshape import CircleShape
from constants import PLAYER_SHOOT_SPEED, SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pg.draw.circle(screen, 'white', self.position, self.radius, 0)

    def update(self, dt):
        self.position += self.velocity * dt

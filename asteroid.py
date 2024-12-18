import pygame as pg
import random as rd

from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pg.draw.circle(screen, 'white', self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = rd.uniform(20.0, 50.0)
        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS  

        split_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        split_asteroid_1.velocity = a * 1.2
        split_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        split_asteroid_2.velocity = b * 1.2
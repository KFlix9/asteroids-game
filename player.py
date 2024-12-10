import pygame as pg

from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED
from circleshape import CircleShape

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self):
        forward = pg.Vector2(0, 1).rotate(self.rotation)
        right = pg.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pg.draw.polygon(screen, "white", self.triangle(), 2)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        print(f'{self.rotation}')

    def update(self, dt):
        keys = pg.key.get_pressed()

        if keys[pg.K_q]:
            self.rotate(dt * -1)
        if keys[pg.K_e]:
            self.rotate(dt) 
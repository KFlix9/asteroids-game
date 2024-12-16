import pygame as pg

from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED,SHOT_RADIUS
from circleshape import CircleShape
from shot import Shot

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
    
    def update(self, dt):
        keys = pg.key.get_pressed()

        if keys[pg.K_F2]:
            self.move(dt)
        if keys[pg.K_w]:
            self.move(dt * -1)
        if keys[pg.K_q]:
            self.rotate(dt * -1)
        if keys[pg.K_e]:
            self.rotate(dt) 
        if keys[pg.K_SPACE]:
            self.shoot(dt) 

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self, dt):
        forward = pg.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self, dt):
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        shot.velocity = pg.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED 

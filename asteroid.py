import pygame
import circleshape as cs
import random

from constants import ASTEROID_MIN_RADIUS

class Asteroid(cs.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius < ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20, 50)
        radius = self.radius - ASTEROID_MIN_RADIUS

        one = Asteroid(self.position.x, self.position.y, radius)
        two = Asteroid(self.position.x, self.position.y, radius)

        one.velocity = self.velocity.rotate(angle)
        two.velocity = self.velocity.rotate(-angle)



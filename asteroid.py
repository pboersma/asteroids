import pygame
import circleshape as cs
from constants import ASTEROID_MAX_RADIUS

class Asteroid(cs.CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y, ASTEROID_MAX_RADIUS)

    def draw(self, display):
        pygame.draw.circle(display, (255, 255, 255), self.position, ASTEROID_MAX_RADIUS, 2)

    def update(self, dt):
        self.position += (100 * dt)

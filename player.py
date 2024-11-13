import pygame

import circleshape as cs
import shot

from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN

class Player(cs.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        
        self.rotation = 0
        self.timer = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        self.timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.timer > 0:
            return False

        shotEntity = shot.Shot(self.position.x, self.position.y)

        # Create initial direction vector (pointing down)
        direction = pygame.Vector2(0, 1)
    
        # Rotate it by player's rotation
        rot_direction = direction.rotate(self.rotation)  # Note the negative sign!

        shotEntity.velocity = rot_direction * PLAYER_SHOOT_SPEED 
        self.timer = PLAYER_SHOOT_COOLDOWN 



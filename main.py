import pygame
import sys
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

# Sprites
import player
import asteroid
import asteroidfield
import shot

def main():
    pygame.init()
    display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    gameClock = pygame.time.Clock()
    dt = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    player.Player.containers = (updateable, drawable)
    playerEntity = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroid.Asteroid.containers = (asteroids, updateable, drawable)

    asteroidfield.AsteroidField.containers = (updateable, )
    asteroidfield.AsteroidField()

    shot.Shot.containers = (shots, updateable, drawable)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        display.fill((0, 0, 0))

        for entity in updateable:
            entity.update(dt)

        for asteroidEntity in asteroids:
            if asteroidEntity.has_collided(playerEntity):
                print('Game over!')
                sys.exit()
            for shotEntity in shots:
                if asteroidEntity.has_collided(shotEntity):
                    shotEntity.kill()
                    asteroidEntity.split()

        for entity in drawable:
            entity.draw(display)
        
        pygame.display.update()
        
        dt = gameClock.tick(60) / 1000

if __name__ == '__main__':
    main()

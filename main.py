import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
import player
import asteroid

def main():
    pygame.init()
    display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    gameClock = pygame.time.Clock()
    dt = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()

    pl = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    at = asteroid.Asteroid(SCREEN_WIDTH / 3, SCREEN_HEIGHT /3)

    updateable.add(pl)
    drawable.add(pl)

    asteroid.add(at)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        display.fill((0, 0, 0))

        for entity in updateable:
            entity.update(dt)

        for entity in drawable:
            entity.draw(display)
        
        pygame.display.update()
        
        dt = gameClock.tick(60) / 1000

if __name__ == '__main__':
    main()

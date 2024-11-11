import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

def main():
    pygame.init()
    display = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        display.fill((0, 0, 0))
        
        pygame.display.update()

if __name__ == '__main__':
    main()

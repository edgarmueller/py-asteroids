import pygame
from constants import *
from player import Player

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, "black")

        for c in updatable:
            c.update(dt)

        for c in drawable:
            c.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()

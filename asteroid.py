import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, PLAYER_RADIUS)
        self.forward = pygame.Vector2(0, 1).rotate(random.randint(-90, 90))

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        self.move(dt)

    def move(self, dt):
        self.position += self.forward * ASTEROID_SPEED * dt

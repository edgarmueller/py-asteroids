import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius = ASTEROID_RADIUS):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, ASTEROID_SPEED).rotate(random.randint(-90, 90))

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        self.move(dt)

    def move(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        print("Splitting asteroid")
        if self.radius <= ASTEROID_MIN_RADIUS:
            print(self.radius)
            return 
        angle = random.randint(20, 50)
        a1_velocity = self.velocity.rotate(angle)
        a2_velocity = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = a1_velocity * 1.2
        a2.velocity = a2_velocity * 1.2

import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (255, 255, 255),  # white
            self.position,
            int(self.radius),
            2
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()  # Always destroy this asteroid

        if self.radius <= ASTEROID_MIN_RADIUS:
            return  # Smallest asteroid, just disappear

        # Otherwise, spawn two smaller asteroids
        random_angle = random.uniform(20, 50)
        velocity1 = self.velocity.rotate(random_angle) * 1.2
        velocity2 = self.velocity.rotate(-random_angle) * 1.2
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        from asteroid import Asteroid  # Avoid circular import issues

        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = velocity1

        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a2.velocity = velocity2

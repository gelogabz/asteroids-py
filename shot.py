import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, PLAYER_SHOOT_SPEED


class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity

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

import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Set containers for Player, Asteroid, and Shot
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable,)

    # Instantiate player (will be added to both groups)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Instantiate asteroid field (will be added to updatable group)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        updatable.update(dt)  # Update all updatables

        # Collision detection: check if player collides with any asteroid
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                pygame.quit()
                return

        # Collision detection: check if any shot collides with any asteroid
        for asteroid in list(asteroids):  # Use list to avoid issues when killing
            for shot in list(shots):
                if asteroid.collides_with(shot):
                    asteroid.split()

        screen.fill((0, 0, 0))
        for obj in drawable:
            obj.draw(screen)   # Draw all drawables
        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()

import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    running = True

    # Time
    game_clock = pygame.time.Clock()
    delta_time = 0

    # Group definitions
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Player definition
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, PLAYER_RADIUS)

    # Asteroid definition
    Asteroid.containers = (asteroids, updatable, drawable)

    # Asteroid field definition
    AsteroidField.containers = updatable
    asteroidfield = AsteroidField()

    # Shot definition
    Shot.containers = (shots, drawable, updatable)

    # Game loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        # Iterate through all drawable objects and draw them
        for drawable_object in drawable:
            drawable_object.draw(screen)

        # Iterate through all updatable objects and update them
        for updatable_object in updatable:
            updatable_object.update(delta_time)

        # Check for collisions between player and asteroids
        for asteroid in asteroids:
            if player.detect_collision(asteroid):
                running = False
                print("Game Over")

        # Check for collisions between shots and asteroids
        for shot in shots:
            for asteroid in asteroids:
                if shot.detect_collision(asteroid):
                    shot.kill()
                    asteroid.split()
                    break

        # Update the display
        pygame.display.flip()

        # Limit frame rate to 60 FPS
        delta_time = game_clock.tick(60) / 1000


if __name__ == "__main__":
    main()

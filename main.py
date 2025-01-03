import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    running = True

    # Time
    game_clock = pygame.time.Clock()
    delta_time = 0

    # Player
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, PLAYER_RADIUS)

    # Game loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        player.draw(screen)
        player.update(delta_time)
        pygame.display.flip()

        # Limit frame rate to 60 FPS
        delta_time = game_clock.tick(60) / 1000


if __name__ == "__main__":
    main()

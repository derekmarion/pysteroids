from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS, ASTEROID_SPEED_INCREASE
import random


class Asteroid(CircleShape):
    """Asteroid class"""

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, delta_time: int):
        self.position += self.velocity * delta_time

    def split(self):
        """Split the asteroid into two smaller asteroids"""

        # Remove original asteroid
        self.kill()

        # If the asteroid is already at the minimum size, don't split
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Create two new asteroids
        angle = random.uniform(20, 50)
        vector_1 = self.velocity.rotate(angle)
        vector_2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_1.velocity = vector_1 * ASTEROID_SPEED_INCREASE
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2.velocity = vector_2 * ASTEROID_SPEED_INCREASE

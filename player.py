from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED
import pygame


class Player(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self):
        """Draw a triangle that represents the player"""

        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        """Draw the player"""
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, delta_time: int):
        """Calculate the rotation of the player"""

        self.rotation += delta_time * PLAYER_TURN_SPEED

    def update(self, delta_time: int):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-delta_time)  # Rotate left
        if keys[pygame.K_d]:
            self.rotate(delta_time)  # Rotate right
        if keys[pygame.K_w]:
            self.move(delta_time)  # Move forward
        if keys[pygame.K_s]:
            self.move(-delta_time)  # Move backward

    def move(self, delta_time: int):
        """Move the player"""

        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * delta_time

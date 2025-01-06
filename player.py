from circleshape import CircleShape
from constants import (
    PLAYER_RADIUS,
    PLAYER_TURN_SPEED,
    PLAYER_SPEED,
    PLAYER_SHOOT_SPEED,
    SHOT_RADIUS,
    PLAYER_SHOT_RATE,
)
import pygame
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0

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

        if keys[pygame.K_SPACE]:
            self.shoot()  # Shoot a bullet

        # Update the shot timer
        if self.shot_timer > 0:
            self.shot_timer -= delta_time

    def move(self, delta_time: int):
        """Move the player"""

        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * delta_time

    def shoot(self):
        """Shoot a bullet"""

        # Prevent player from shooting if the shot timer is greater than 0
        if self.shot_timer > 0:
            return

        # Create a bullet at the player's position
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)

        # Set the bullet's vector to the player's forward vector
        forward = pygame.Vector2(0, 1).rotate(self.rotation)

        # Set the bullet's velocity
        shot.velocity = forward * PLAYER_SHOOT_SPEED

        # Reset the shot timer
        self.shot_timer = PLAYER_SHOT_RATE

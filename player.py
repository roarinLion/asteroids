import pygame

from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_SPEED


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0  # Initialize rotation

    def draw(self, screen):
        """Draws a triangle representing the player on the given screen."""
        triangle = self.triangle()  # Call to the internal triangle method
        pygame.draw.polygon(screen, (255, 255, 255), triangle)

    def triangle(self):
        """Generates coordinates for a triangle centered on the player.

        Returns:
            list of pygame.Vector2: Three points defining the triangle.
        """
        forward = pygame.Vector2(0, -1).rotate(
            self.rotation
        )  # Negative y for correct upward orientation
        right = pygame.Vector2(1, 0).rotate(self.rotation) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius / 2 - right
        c = self.position - forward * self.radius / 2 + right
        return [a, b, c]

    def rotate(self, dt):
        """Rotates the player by dt radians."""
        self.rotation = dt * PLAYER_SPEED

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt)
        if keys[pygame.K_d]:
            self.rotate(-dt)

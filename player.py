import pygame
from collisions import handle_collisions

class Player:
    def __init__(self):
        self.hitbox = pygame.Rect(64, 64, 28, 28)
        self.speed = 3

    def move(self, keys, environment):
        dx, dy = 0, 0
        if keys[pygame.K_w]:
            dy -= self.speed
        if keys[pygame.K_s]:
            dy += self.speed
        if keys[pygame.K_a]:
            dx -= self.speed
        if keys[pygame.K_d]:
            dx += self.speed

        handle_collisions(self.hitbox, dx, dy, environment)

    def draw(self, screen):
        pygame.draw.rect(screen, (255,255,255), self.hitbox)
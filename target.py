import pygame

class Target:
    def __init__(self):
        self.hitbox = pygame.Rect(128, 128, 32, 32)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.hitbox)
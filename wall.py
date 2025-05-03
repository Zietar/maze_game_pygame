import pygame

class Wall:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hitbox = pygame.Rect(self.x, self.y, 32, 32)

    def draw(self, screen):
        pygame.draw.rect(screen, (215,150,180), self.hitbox)
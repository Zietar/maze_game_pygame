# 3 poziomy

# custom określanie gdzie pojawi się teren, gracz, target

# teren
# gracz

import pygame
from player import Player
from level_manager import load_level
from target import Target

# pygame initialization
pygame.init()
screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True

# objects initialization
player = Player()
target_1 = Target()
target_1_active = True

target_2 = Target()
target_2_active = False


environment = load_level("level_1", player, target_1)

while running:

    # game logic
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    player.move(keys, environment)

    # game rendering
    screen.fill((255,190,220))

    player.draw(screen)

    for object in environment:
        object.draw(screen)

    if target_1_active:
        target_1.draw(screen)
    if target_2_active:
        target_2.draw(screen)

    if player.hitbox.colliderect(target_1.hitbox):
        target_1_active = False
        target_2_active = True
        environment = load_level("level_2", player, target_2)
    if player.hitbox.colliderect(target_2.hitbox):
        target_2_active = False
        environment = load_level("level_3", player)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
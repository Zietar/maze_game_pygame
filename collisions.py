
def handle_collisions(player_hitbox, dx, dy, environment):

    # horizontal
    player_hitbox.x += dx

    for object in environment:

        if player_hitbox.colliderect(object.hitbox):

            if dx > 0:
                player_hitbox.right = object.hitbox.left

            if dx < 0:
                player_hitbox.left = object.hitbox.right

    # vertical
    player_hitbox.y += dy
    for object in environment:

        if player_hitbox.colliderect(object.hitbox):

            if dy > 0:
                player_hitbox.bottom = object.hitbox.top
                
            if dy < 0:
                player_hitbox.top = object.hitbox.bottom

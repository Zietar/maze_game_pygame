from wall import Wall
from target import Target
from player import Player

level_1 = [
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        "W       W       W          W           W",
        "W WWWWW W WWWWW  W WWWWWW  W WWWWWW WW W",
        "W W     W     W  W      W  W W      W  W",
        "W W WWWWW WWW W W WWWW  W  W W WWWW W  W",
        "W W     W   W W         W      W    W  W",
        "W WWWWW WWW W WWWWW  W  WWWW W W WWWW  W",
        "W     W     W     W  W      W   W      W",
        "WWWWW WWWWWWW WWWWW  WWWWWW W W W WWWW W",
        "W P W       W     W      W  W W W      W",
        "W W WWW WWWWWWWWW  WWWWW W WW W WWWWW  W",
        "W W   W   W     W      W W    W     W  W",
        "W WWWWW W W WWW WWWWW  W WWWWWWWWW   W W",
        "W       W           W      W     W W   W",
        "WWWWW W WWWWWWW WWWWW  WWWWW WWWWW WW  W",
        "W     W       W     W        W     W   W",
        "W WWWWW WWWWWWW WWWWWWWW WWWWW WWWWW W W",
        "W     W     W              W     W     W",
        "W WWWWW WWWWWWWWWWW W WWW  WWWWWWW W W W",
        "W     W           W W   W         W    W",
        "W WWWWWWWWW     WWWW   WWWWWW WWWWWW   W",
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW  W",
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWTW",
    ]

level_2 = [
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        "W P   W     W       W         W        W",
        "W WWWWW WWW WWW WWWWW WWW WW WWWWWWW W W",
        "W     W   W   W     W     W       W    W",
        "WWWWW WWWWWWW W WWW WWWWW WWWWWW W W W W",
        "W   W                   W     W  W W   W",
        "W W WWWWWWWWW WWW WWWWW WWWWW WW W WW  W",
        "W W             W     W     W W  W     W",
        "W WWWWWWW WWWW WW W W WWWWWWW WW WWW W W",
        "W     W     W     W W     W    W      WW",
        "WWWWW WWWWW W WWW W WWWWW WW WWWWWW W  W",
        "W     W     W     W     W       W W W  W",
        "W WWWWW WWWWWWWWW WWW WWWWWWWWW   W    W",
        "W     W W     W     W     W     W W WWW",
        "WWWWW W W WWWWWWWWWWW W WWWWWWWWW W    W",
        "W   W                 W         W   W  W",
        "W WWWWWWWWWW WWWWWWWW WWWW   WWWWWWWW  W",
        "W                WW           W        W",
        "W WWWWWWWWWWWWWWWWWWWWWWWW  WWW WWWW  WW",
        "W  WW        WWWWWWWW      WWW  WWWWW  W",
        "W      WWWWW                   WW      W",
        "WWWWWWWWWWWWWW  WWWWWWWWWWWWWWWWWWWWWWWW",
        "WWWWWWWWWWWWWWTWWWWWWWWWWWWWWWWWWWWWWWWW",
    ]

level_3 = [
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        "W                                      W",
        "W   W   W WWWWW  W   W                 W",
        "W    W W  W   W  W   W                 W",
        "W     W   W   W  W   W                 W",
        "W     W   WWWWW  WWWWW                 W",
        "W                                      W",
        "W                                      W",
        "W   W     W  W  W     W                W",
        "W   W     W  W  WW    W                W",
        "W   W     W  W  W W   W                W",
        "W   W  W  W  W  W  W  W                W",
        "W   W W W W  W  W   W W         P      W",
        "W   WW   WW  W  W    WW                W",
        "W   W     W  W  W     W                W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    ]

def load_level(level, player, target=None):

    layout = []

    x = y = 0

    if level == "level_1":
        my_level = level_1
    elif level == "level_2":
        my_level = level_2
    elif level == "level_3":
        my_level = level_3

    for row in my_level:

        for col in row:

            if col == "W":
                layout.append(Wall(x, y))
            elif col == "T":
                target.x = x
                target.y = y
                target.hitbox.topleft = (x, y)
            elif col == "P":
                player.x = x
                player.y = y
                player.hitbox.topleft = (x, y)

            x += 32

        y += 32
        x = 0

    return layout

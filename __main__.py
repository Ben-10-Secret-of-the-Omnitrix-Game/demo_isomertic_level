import pygame
import sys
from .tile import Tile

MAPWIDTH = 3
MAPHEIGH = 3
TILESIZE = 50


BLACK = (0, 0, 0)
BROWN = (153, 76, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)

surface = object
tilemap = [
    [Tile(BROWN, 0, 0), Tile(BROWN, 1, 0), Tile(BROWN, 2, 0)],
    [Tile(BROWN, 0, 1), Tile(BROWN, 1, 1), Tile(BROWN, 2, 1)],
    [Tile(BROWN, 0, 2), Tile(BROWN, 1, 2), Tile(BROWN, 2, 2)],
]


def render_tilemap():
    global surface
    for x in range(MAPHEIGH):
            for y in range(MAPWIDTH):
                tile = tilemap[y][x]
                tile: Tile
                print(x, y)
                pygame.draw.rect(surface, tile.color, (x * TILESIZE, y * TILESIZE, TILESIZE, TILESIZE))


def game_loop_handler():
    render_tilemap()
    pygame.display.update()






if __name__ == "__main__":
    pygame.init()
    surface = pygame.display.set_mode((MAPWIDTH * TILESIZE, MAPHEIGH * TILESIZE));
    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        game_loop_handler()


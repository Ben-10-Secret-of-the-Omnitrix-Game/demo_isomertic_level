import pygame
import sys
import os

from tile import Tile

MAPWIDTH = 3
MAPHEIGHT = 4
TILESIZE = 50

wall_graphic_height = 98
floor_graphic_wdth = 103
floor_graphic_height = 53
wall_height = wall_graphic_height - floor_graphic_height
border_offset = 150

BLACK = (0, 0, 0)
BROWN = (153, 76, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


def load_resource_image(name, colorkey=None):
    path = os.path.join("resources\\images", f"{name}.png")
    print(path)
    image = pygame.image.load(path)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


game_screen = object
wall = object
floor = object

tilemap = []


def render_basic_tilemap():
    global game_screen
    for y in range(MAPWIDTH):
        for x in range(MAPHEIGHT):
            tile = tilemap[x][y]
            tile: Tile
            pygame.draw.rect(game_screen, tile.color,
                             (x * TILESIZE, y * TILESIZE, TILESIZE, TILESIZE))


def render_isometric_tilemap():
    global game_screen, wall
    for y in range(MAPWIDTH):
        for x in range(MAPHEIGHT):
            tile = tilemap[x][y]
            tile: Tile
            render_isometric_tile(tile, x, y)

    pygame.display.flip()


def render_isometric_tile(tile, x, y):
    cart_x = x * TILESIZE
    cart_y = y * TILESIZE
    iso_x, iso_y = cartesian_to_isometric(cart_x, cart_y)
    game_screen.blit(tile.texture, (iso_x + border_offset, iso_y + border_offset - wall_height))


def cartesian_to_isometric(x, y):
    isometric_x = x - y
    isometric_y = (x + y) / 2
    return isometric_x, isometric_y


def game_loop_handler():
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    # Different types of rendering
    # render_basic_tilemap()
    render_isometric_tilemap()
    pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    game_screen = pygame.display.set_mode(
        (600, 400))

    wall = load_resource_image("block")
    floor = load_resource_image("floor")

    tilemap = [
        [Tile(BROWN, 0, 0, wall), Tile(
            BROWN, 0, 1, wall), Tile(BROWN, 0, 2, wall)],
        [Tile(BROWN, 1, 0, wall), Tile(
            GREEN, 1, 1, floor), Tile(BROWN, 1, 2, wall)],
        [Tile(BROWN, 2, 0, wall), Tile(
            GREEN, 2, 1, floor), Tile(BROWN, 2, 2, wall)],
        [Tile(BROWN, 3, 0, wall), Tile(
            BROWN, 3, 1, wall), Tile(BROWN, 3, 2, wall)],
    ]
    while True:
        game_loop_handler()

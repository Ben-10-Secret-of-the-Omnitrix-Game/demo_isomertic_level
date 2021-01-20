import pygame
import sys
import os

from tile import Tile
from player import Player

MAPWIDTH = 5
MAPHEIGHT = 5
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
players = []


def render_players():
    global game_screen, players
    for player in players:
        x, y = player.x, player.y
        game_screen.blit(player.texture, players_place(player, get_cell_center(x, y)))


def get_cell_center(x, y):
    cart_x = (x + 1) * TILESIZE + border_offset
    cart_y = (y - 1) * TILESIZE + border_offset - wall_height
    cntr_x = cart_x + TILESIZE // 2
    cntr_y = cart_y + TILESIZE // 2
    return cartesian_to_isometric(cart_x, cntr_y)


def players_place(player, pos):
    x = pos[0]
    y = pos[1]
    return x, y - player.height + 20


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
    game_screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.image.save(game_screen, 'hi_man.png')
            pygame.quit()
            sys.exit()
        s = list(pygame.key.get_pressed())[79: 83]
        if 1 in s:
            if s[2]:
                ben.x += 1
                ben.change_rotate(0)
            elif s[3]:
                ben.x -= 1
                ben.change_rotate(2)
            elif s[1]:
                ben.y += 1
                ben.change_rotate(3)
            else:
                ben.y -= 1
                ben.change_rotate(1)

    # Different types of rendering
    # render_basic_tilemap()
    render_isometric_tilemap()
    render_players()
    pygame.display.flip()


if __name__ == "__main__":
    pygame.init()
    game_screen = pygame.display.set_mode(
        (600, 400))

    wall = load_resource_image("block")
    floor = load_resource_image("floor")
    ben_images_png = ["ben10_1", "ben10_2", "ben10_3", "ben10_4"]
    ben_images = [load_resource_image(i) for i in ben_images_png]
    ben = Player('Ben', ben_images, 4, 2)
    players.append(ben)

    clock = pygame.time.Clock()
    fps = 1

    for row in range(MAPHEIGHT):
        stock = []
        for col in range(MAPWIDTH):
            if row == 0 or row == MAPHEIGHT - 1:
                stock.append(Tile(BROWN, row, col, wall))
            elif col == 0 or col == MAPWIDTH - 1:
                stock.append(Tile(BROWN, row, col, wall))
            else:
                stock.append(Tile(GREEN, row, col, floor))
        tilemap.append(stock)
    while True:
        game_loop_handler()

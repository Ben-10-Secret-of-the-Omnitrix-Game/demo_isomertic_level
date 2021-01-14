import pygame

class Tile:

    def __init__(self, color, x, y):
        """
        color - tuple of (r, g, b) or (r, g, b, a)
        x and y are all cartesian coordinates 
        """
        assert len(color) in (3, 4), "type help(Tile) to see constructor variables format"
        self.color = pygame.Color(color)
        self.x = x
        self.y = y

    
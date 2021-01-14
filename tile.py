import pygame

class Tile:

    def __init__(self, color, x, y, image=None):
        """
        color - tuple of (r, g, b) or (r, g, b, a)
        x and y are all cartesian coordinates 
        """
        assert len(color) in (3, 4), "type help(Tile) to see constructor variables format"
        assert isinstance(image, pygame.Surface), image
        self.color = pygame.Color(color)
        self.x = x
        self.y = y
        self.texture = image

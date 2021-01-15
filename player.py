import pygame


class Player:
    def __init__(self, name, image=None, x=0, y=0):
        """
        x, y - cell
        """
        assert isinstance(image, pygame.Surface), image
        self.texture = image
        self.name = name
        self.x = x
        self.y = y
        self.width, self.height = image.get_size()

import pygame


class Player:
    def __init__(self, name, image=None, x=0, y=0):
        """
        x, y - cell
        """
        self.rotate = 0
        self.image = image
        if image:
            self.texture = image[self.rotate]
        self.name = name
        self.x = x
        self.y = y
        self.width, self.height = self.texture.get_size()

    def change_rotate(self, rotate):
        self.rotate = rotate
        if self.image:
            self.texture = self.image[self.rotate]
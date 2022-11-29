import pygame
from game_object import GameObject

# This class extends GameObject
class Invader(GameObject):
    # method 1
    def __init__(self, x, y, image, point_value, is_destroyed = False):
        super().__init__(x, y, image)
        self.point_value = point_value
        # default value is false when object created
        # destroyed method will change value to true if alien has been shot
        self.is_destroyed = is_destroyed

    # method 2
    def move(self):
        # Invaders move left and right, and shift downw each time they reach a screen edge
        pass

    # method 3
    def update_destroyed(self):
        # Updates is_destroyed attribute to true if invader has been shot by laser
        pass


rows = 3
columns = 10

# Instantiate 3 rows of invaders with the top row worth 30 pts, the middle row worth 20 pts, and the bottom row worth 10 pts
points = 10
def create_invaders():
    for row in range(rows):
        for position in range(columns):
            invader = Invader(100 + position * 100, 100 + row * 50, 'invader.png', points * (3 - row))

create_invaders()


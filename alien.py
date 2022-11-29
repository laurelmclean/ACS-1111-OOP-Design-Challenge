import pygame
from game_object import GameObject

# This class extends GameObject
class Alien(GameObject):
    # method 1
    def __init__(self, x, y, image, point_value, is_destroyed = False):
        super().__init__(x, y, image)
        self.point_value = point_value
        # default value is false when object created
        # destroyed method will change value to true if alien has been shot
        self.is_destroyed = is_destroyed

    # method 2
    def move(self):
        # Aliens move left and right, and shift downw each time they reach a screen edge
        pass

    # method 3
    def update_destroyed(self):
        # Updates is_destroyed attribute to true if Alien has been shot by laser
        pass


# Here are the different types of aliens and their point value - we can use to instantiate the objects
# Bottom invaders–10 points
# Middle invaders–20 points
# Top invaders–30 points
# UFO–50, 100, 150, or 300 points
# Extra laser base–1000 points

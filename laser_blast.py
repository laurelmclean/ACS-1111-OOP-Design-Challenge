import pygame
from game_object import GameObject

# This class extends GameObject
class Laser_blast(GameObject):
    # method 1
    def __init__(self, x, y, image, damage):
        super().__init__(x, y, image)
        self.damage = damage

    # method 2
    def check_for_hit(self):
        # Monitor if the laser blast collides with the player
        pass

    # method 3
    def inflict_damage(self):
        # Update the player's health by subtracting damage points
        pass
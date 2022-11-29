import pygame
from game_object import GameObject

# This class extends GameObject
class Player(GameObject):
    # method 1
    def __init__(self, x, y, image, health):
        super().__init__(x, y, image)
        self.starting_health = health
        self.remaining_health = health

    # method 2
    def update_position(self):
        # Update the player's position based on keys pressed
        pass

    # method 3
    def update_health(self):
        # Updates the player's health based on scoring and receiving laser blasts
        pass

# instantiate a player at bottom of screen with three lives
player = Player(250, 500, 'player.png', 3)


    
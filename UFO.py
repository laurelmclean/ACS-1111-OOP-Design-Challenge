import pygame
from game_object import GameObject
from invader import Invader

# This class extends GameObject and is composed of invaders
class UFO(GameObject):
    # method 1
    def __init__(self, x, y, image, point_value, num_invaders, is_destroyed=False):
        super().__init__(x, y, image)
        self.point_value = point_value
        self.num_invaders = num_invaders
        self.is_destroyed = is_destroyed
        self.invaders = []

    # method 2 - adds invader to UFO
    def add_invader(self, invader):
        self.invaders.append(invader)

    # method 3
    def update_destroyed(self):
        # Updates is_destroyed attribute to true if UFO has been shot by laser
        pass
    
# instantiate new UFO object worth 150 points and composed of 3 invaders
new_ufo = UFO(0, 0, 'ufo.png', 150, 3)

# demonstrate adding three invaders to UFO

invader_1 = Invader(0, 0, 'invader.png', 50)
new_ufo.add_invader(invader_1)

invader_2 = Invader(0, 0, 'invader.png', 50)
new_ufo.add_invader(invader_2)

invader_3 = Invader(0, 0, 'invader.png', 50)
new_ufo.add_invader(invader_3)

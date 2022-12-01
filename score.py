import pygame
from game_object import GameObject

# This class extends GameObject    
class Score(GameObject):
    def __init__(self, x, y, text_size=24, text_colour=(0,0,0), score=0):
        super().__init__(x, y)
        self.score = score

    def set_score(player_health, laser_damage):
        pass


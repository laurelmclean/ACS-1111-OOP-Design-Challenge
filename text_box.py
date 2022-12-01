import pygame
from game_object import GameObject

# This class extends GameObject    
class Text_box(GameObject):
    def __init__(self, x, y, width, height, text_size=24, text_colour=(0,0,0)):
        super().__init__(x, y)
        self.width = width
        self.height = height
        self.active = False
        self.text = ""
        self.text_size = text_size
        self.font = pygame.font.SysFont("Helvetica", self.text_size)
        self.text_colour = text_colour

    def draw(self, gameDisplay):
        # Display the text box
            pass
                
    def add_text(self, key):
        # append characters (keys pressed) to self.text as they are enterred in the text box
        pass

    # Returns the user input from the text box
    def return_value(self):
        return self.text
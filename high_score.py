import pygame
from score import Score
from text_box import Text_box

# This class extends Score and Text_box   
class High_score(Score, Text_box):
    def __init__(self, x, y, text_size=24, text_colour=(0,0,0), user_name=""):
        super().__init__(x, y, text_size=24, text_colour=(0,0,0))
        self.user_name = user_name
        self.__user_password = ""

        # This method overides the Text_box draw method with different size and colours
        def draw(self, gameDisplay):
        # Display the text box
            pass

        # This method overides the Text_box get_text method with the additional security feature
        # of concealing the password enterred
        def get_text(self, key):
        # append characters (keys pressed) to self.text as they are enterred in the text box
        # but display *s instead of the characters
            pass

        def get_user_password():
            pass

        def show_high_score(user_name, score):
            pass
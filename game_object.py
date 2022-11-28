# Import and initalize pygame
import pygame
pygame.init()

# Game Object
# This class extends pygame.sprite.Sprite (built in pygame class)
class GameObject(pygame.sprite.Sprite):
  # method 1
  def __init__(self, x, y, image):
    super(GameObject, self).__init__()
    # displays image
    self.surf = pygame.image.load(image)  
    # x and y coordinates
    self.x = x
    self.y = y

# method 2
# copies the pixels onto the screen which allows it to show up on pygame
  def render(self, screen):
    screen.blit(self.surf, (self.x, self.y))

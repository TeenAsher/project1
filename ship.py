# The class Ship with starring Diana
import pygame.image
from pygame import *

class Ship:
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """Initializes the ship and its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen_rect()

        self.image = pygame.image.load('dianaF.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draws the ship in its current location"""
        self.screen.blit(self.image, self.rect)
        
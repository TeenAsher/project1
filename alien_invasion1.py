# ------------------------------------
# First file of the project №1 'Alien Invasion'
# 'Alien Invasion' - game from the book 'Python Crash Course' by Eric Matthes
# Code by TeenAsher
# ------------------------------------
import pygame
from pygame import *
import sys
from settings import Settings

class AlienInvasion:
    """Overall class to manage game's assets and behavior"""

    def __init__(self):
        """Initializes the pygame and creates the game's resources"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height), 0, 32)
        pygame.display.set_caption('Alien Invasion')

    def run_game(self):
        """Start the main loop for the game"""
        while True:

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.fill(self.settings.bg_colour)
            pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
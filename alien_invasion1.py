# ------------------------------------
# First file of the project №1 'Alien Invasion'
# 'Alien Invasion' - game from the book 'Python Crash Course' by Eric Matthes
# Code by TeenAsher
# ------------------------------------
import pygame
from pygame import *
import sys

class AlienInvasion:
    """Overall class to manage game's assets and behavior"""

    def __init__(self):
        """Initialises the pygame and creates the game's resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800), 0, 32)
        pygame.display.set_caption('Alien Invasion')
        self.bg_colour = (230, 100, 115)

    def run_game(self):
        """Start the main loop for the game"""
        while True:

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.fill(self.bg_colour)
            pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
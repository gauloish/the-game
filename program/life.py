""" Life

Class Life to emulate life to entities with a sprint
"""

import pygame

from .functions import getPath


class Life:
    """Life To Entities

    Attributes:
        screen: pygame.Surface
        image: pygame.Surface
        rect: pygame.Rect
        screen_rect: pygame.Rect
        centerx: int
        bottom: int
    """

    def __init__(self, screen, center, bottom):
        """Initialize Bullet

        Args:
            screen (pygame.Surface): game screen
            center (int): horizontal center position of image
            bottom (int): vertical bottom position of image
        """

        self.screen = screen

        self.image = pygame.image.load(getPath("images/life/life.png"))

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = center
        self.rect.bottom = bottom

    def blitme(self):
        """Show Image of Life"""

        self.screen.blit(self.image, self.rect)

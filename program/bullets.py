""" Bullets

Class Bullet to emulate a bullet with physics and a sprint
"""

import pygame

from .functions import getPath


class Bullet:
    """Bullet To Game

    Attributes:
        screen: pygame.Surface
        image: pygame.Surface
        rect: pygame.Rect
        screen_rect: pygame.Rect
        centerx: int
        bottom: int
        moving: bool
        velocity: int
    """

    def __init__(self, screen: pygame.Surface, center: int, bottom: int) -> None:
        """Initialize Bullet

        Args:
            screen (pygame.Surface): game screen
            center (int): horizontal center position of image
            bottom (int): vertical bottom position of image
        """

        self.screen = screen

        self.image = pygame.image.load(getPath("images/munition/bullet.png"))

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = center
        self.rect.bottom = bottom

        self.moving = False

        self.velocity = 1

    def blitme(self) -> None:
        """Show Image of Bullet"""

        self.screen.blit(self.image, self.rect)

    def update(self, center: int, bottom: int) -> None:
        """Update Bullet Position

        Args:
            center (int): horizontal center position of image
            bottom (int): vertical bottom position of image
        """

        if self.moving:
            self.rect.bottom -= self.velocity
        else:
            self.rect.centerx = center
            self.rect.bottom = bottom - 72

        if self.rect.bottom <= 0:
            self.moving = False

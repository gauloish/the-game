import pygame

from .utils import resolve


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

    def __init__(self, screen: pygame.Surface, center: int, bottom: int) -> None:
        """Initialize Bullet

        Args:
            screen (pygame.Surface): game screen
            center (int): horizontal center position of image
            bottom (int): vertical bottom position of image
        """

        self.screen = screen

        self.image = pygame.image.load(resolve("images/life/life.png"))

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = center
        self.rect.bottom = bottom

    def blitme(self) -> None:
        """Show Image of Life"""

        self.screen.blit(self.image, self.rect)

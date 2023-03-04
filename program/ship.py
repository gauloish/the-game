import pygame

from .utils import resolve
from .life import Life
from .bullets import Bullet

colors = {
    0: resolve("images/ships/ship_red.png"),
    1: resolve("images/ships/ship_pink.png"),
    2: resolve("images/ships/ship_purple.png"),
    3: resolve("images/ships/ship_blue.png"),
    4: resolve("images/ships/ship_green.png"),
}


class Ship:
    """Ship

    Attributes:
        screen: pygame.Surface
        color: int
        image: pygame.Surface
        rect: pygame.Rect
        screen_rect: pygame.Rect
        centerx: int
        bottom: int
        moving_left: bool
        moving_right: bool
        life: int
        velocity: int
        bullet: Bullet
    """

    def __init__(
        self, screen: pygame.Surface, color: int, velocity: int, life: int
    ) -> None:
        """Initialize ship

        Args:
            screen (pygame.Surface): game screen
            color (int): ship color number
            velocity (int): ship velocity
            life (int): ship life
        """

        self.screen = screen
        self.color = color

        self.image = pygame.image.load(colors[color])

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 50

        self.moving_left = False
        self.moving_right = False

        self.life = life

        if self.life == 1:
            self.lifes = [
                Life(screen, self.rect.centerx + 30 * n, 780) for n in range(0, life)
            ]
        elif self.life == 3:
            self.lifes = [
                Life(screen, self.rect.centerx - 29 + 30 * n, 780)
                for n in range(0, life)
            ]
        elif self.life == 5:
            self.lifes = [
                Life(screen, self.rect.centerx - 59 + 30 * n, 780)
                for n in range(0, life)
            ]

        self.velocity = velocity

        self.bullet = Bullet(screen, self.rect.centerx, self.rect.bottom)

    def blitme(self) -> None:
        """Show image of ship"""

        self.screen.blit(self.image, self.rect)

        for life in self.lifes:
            life.blitme()

    def update(self) -> None:
        """Update ship position"""

        if self.moving_left and self.rect.centerx >= 35:
            self.rect.centerx -= self.velocity

            for life in self.lifes:
                life.rect.centerx -= self.velocity

        if self.moving_right and self.rect.centerx <= 1165:
            self.rect.centerx += self.velocity

            for life in self.lifes:
                life.rect.centerx += self.velocity

    def hit(self) -> None:
        """Verify hit in enemy"""

        self.life -= 1

        if self.life % 2 == 0:
            del self.lifes[-1]
        else:
            del self.lifes[0]

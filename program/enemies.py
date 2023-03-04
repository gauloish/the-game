import pygame

from .utils import resolve
from .life import Life
from .ship import Ship

colors_pawn = {
    0: resolve("images/enemies/pawn/pawn_blue.png"),
    1: resolve("images/enemies/pawn/pawn_pink.png"),
    2: resolve("images/enemies/pawn/pawn_yellow.png"),
}

colors_knight = {
    0: resolve("images/enemies/knight/knight_blue.png"),
    1: resolve("images/enemies/knight/knight_green.png"),
    2: resolve("images/enemies/knight/knight_red.png"),
    3: resolve("images/enemies/knight/knight_yellow.png"),
}

colors_bishop = {
    0: resolve("images/enemies/bishop/bishop_blue.png"),
    1: resolve("images/enemies/bishop/bishop_green.png"),
    2: resolve("images/enemies/bishop/bishop_pink.png"),
    3: resolve("images/enemies/bishop/bishop_purple.png"),
}


class Pawn:
    """Pawn Enemy

    Attributes:
        screen: pygame.Surface
        color: int
        image: pygame.Surface
        rect: pygame.Rect
        screen_rect: pygame.Rect
        centerx: int
        bottom: int
        life: int
        velocity: int
    """

    def __init__(
        self, screen: pygame.Surface, color: int, center: int, velocity: int, life: int
    ) -> None:
        """Pawn initialize

        Args:
            screen (pygame.Surface): game screen
            color (int): color number
            center (int): horizontal center position of image
            velocity (int): velocity of pawn
            life (int): life amount
        """

        self.screen = screen
        self.color = color

        self.image = pygame.image.load(colors_pawn[color])

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = center
        self.rect.bottom = 0

        self.life = life

        if self.life == 1:
            self.lifes = [Life(screen, center, self.rect.bottom - 50)]
        elif self.life == 2:
            self.lifes = [
                Life(screen, center - 16, self.rect.bottom - 50),
                Life(screen, center + 16, self.rect.bottom - 50),
            ]

        self.velocity = velocity

    def blitme(self) -> None:
        """Show image of pawn"""

        self.screen.blit(self.image, self.rect)

        for life in self.lifes:
            life.blitme()

    def move(self) -> None:
        """Move pawn

        Args:
            velocity (int): velocity of pawn
        """

        self.rect.bottom += self.velocity

        for life in self.lifes:
            life.rect.bottom += self.velocity

    def colision(self, ship: Ship) -> None:
        """Verify colision in bullets, ship or back

        Args:
            ship (Ship): ship controlled by user
        """

        if ship.bullet.moving:
            if (
                self.rect.centerx - 27
                <= ship.bullet.rect.centerx
                <= self.rect.centerx + 27
            ):
                if ship.bullet.rect.bottom <= self.rect.bottom - 8:
                    self.life -= 1

                    del self.lifes[-1]

                    ship.bullet.moving = False

    def invade(self) -> bool:
        """Verify invasion by pawn

        Returns:
            bool: invasion state
        """

        if self.rect.bottom >= 800:
            return True
        else:
            return False

    def death(self) -> bool:
        """Verify pawn death

        Returns:
            bool: death state
        """

        if self.life <= 0:
            return True
        else:
            return False


class Knight:
    """Knight Enemy

    Attributes:
        screen: pygame.Surface
        color: int
        image: pygame.Surface
        rect: pygame.Rect
        screen_rect: pygame.Rect
        centerx: int
        bottom: int
        life: int
        velocity: int
    """

    def __init__(
        self, screen: pygame.Surface, color: int, center: int, velocity: int, life: int
    ) -> None:
        """Knight initialize

        Args:
            screen (pygame.Surface): game screen
            color (int): color number
            center (int): horizontal center position of image
            velocity (int): velocity of knight
            life (int): life amount
        """

        self.screen = screen
        self.color = color

        self.image = pygame.image.load(colors_knight[color])

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = center
        self.rect.bottom = 0

        self.life = life

        if self.life == 1:
            self.lifes = [Life(screen, center, self.rect.bottom - 70)]
        elif self.life == 2:
            self.lifes = [
                Life(screen, center - 16, self.rect.bottom - 70),
                Life(screen, center + 16, self.rect.bottom - 70),
            ]

        self.velocity = velocity

    def blitme(self) -> None:
        """Show image of knight"""

        self.screen.blit(self.image, self.rect)

        for life in self.lifes:
            life.blitme()

    def move(self) -> None:
        """Move knight

        Args:
            velocity (int): velocity of knight
        """

        self.rect.bottom += self.velocity

        for life in self.lifes:
            life.rect.bottom += self.velocity

    def colision(self, ship: Ship) -> None:
        """Verify colision in bullets or ship

        Args:
            ship (Ship): ship controlled by user
        """

        if ship.bullet.moving:
            if (
                self.rect.centerx - 31
                <= ship.bullet.rect.centerx
                <= self.rect.centerx + 31
            ):
                if ship.bullet.rect.bottom <= self.rect.bottom - 20:
                    self.life -= 1

                    del self.lifes[-1]

                    ship.bullet.moving = False

    def invade(self) -> bool:
        """Verify invasion by knight

        Returns:
            bool: invasion state
        """

        if self.rect.bottom >= 800:
            return True
        else:
            return False

    def death(self) -> bool:
        """Verify knight death

        Returns:
            bool: death state
        """

        if self.life <= 0:
            return True
        else:
            return False


class Bishop:
    """Bishop Enemy

    Attributes:
        screen: pygame.Surface
        color: int
        image: pygame.Surface
        rect: pygame.Rect
        screen_rect: pygame.Rect
        centerx: int
        bottom: int
        life: int
        velocity: int
    """

    def __init__(
        self, screen: pygame.Surface, color: int, center: int, velocity: int, life: int
    ) -> None:
        """Knight Initialize

        Args:
            screen (pygame.Surface): game screen
            color (int): color number
            center (int): horizontal center position of image
            velocity (int): velocity of bishop
            life (int): life amount
        """

        self.screen = screen
        self.color = color

        self.image = pygame.image.load(colors_bishop[color])

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = center
        self.rect.bottom = 0

        self.life = life

        if self.life == 1:
            self.lifes = [Life(screen, center, self.rect.bottom - 70)]
        elif self.life == 2:
            self.lifes = [
                Life(screen, center - 16, self.rect.bottom - 70),
                Life(screen, center + 16, self.rect.bottom - 70),
            ]

        self.velocity = velocity

    def blitme(self) -> None:
        """Show image of bishop"""

        self.screen.blit(self.image, self.rect)

        for life in self.lifes:
            life.blitme()

    def move(self) -> None:
        """Move Bishop

        Args:
            velocity (int): velocity of bishop
        """

        self.rect.bottom += self.velocity

        for life in self.lifes:
            life.rect.bottom += self.velocity

    def colision(self, ship: Ship) -> None:
        """Verify colision in bullets or ship

        Args:
            ship (Ship): ship controlled by user
        """

        if ship.bullet.moving:
            if (
                self.rect.centerx - 45
                <= ship.bullet.rect.centerx
                <= self.rect.centerx + 45
            ):
                if ship.bullet.rect.bottom <= self.rect.bottom - 12:
                    self.life -= 1

                    del self.lifes[-1]

                    ship.bullet.moving = False

    def invade(self) -> bool:
        """Verify invasion by bishop

        Returns:
            bool: invasion state
        """

        if self.rect.bottom >= 800:
            return True
        else:
            return False

    def death(self) -> bool:
        """Verify bishop death

        Returns:
            bool: death state
        """

        if self.life <= 0:
            return True
        else:
            return False

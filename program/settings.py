""" Settings

General settings to Game
"""


class Settings:
    """Settings to Game

    Attributes:
        width: int
        height: int
        back: list[int]
        display: str
    """

    def __init__(self):
        """Initialize Settings"""

        self.width = 1200
        self.height = 80

        self.back = [230, 230, 230]

        self.display = "The Game"

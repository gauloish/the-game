""" Settings

General settings to Game
"""


class Settings:
    """Settings to Game

    Attributes:
        width: int
        height: int
        delay: int
        back: list[int]
        display: str
        amounts: dict[str, dict[str, dict[str, int]]]
    """

    def __init__(self) -> None:
        """Initialize Settings"""

        self.width = 1200
        self.height = 800
        self.delay = 50

        self.back = [230, 230, 230]

        self.display = "The Game"

        self.amounts = {
            "easy": {
                "ship": {"velocity": 1, "life": 1},
                "pawns": {"velocity": 2, "life": 1, "amount": 10},
                "knights": {"velocity": 2, "life": 1, "amount": 8},
                "bishops": {"velocity": 2, "life": 1, "amount": 6},
            },
            "medium": {
                "ship": {"velocity": 1, "life": 1},
                "pawns": {"velocity": 1, "life": 1, "amount": 12},
                "knights": {"velocity": 2, "life": 1, "amount": 10},
                "bishops": {"velocity": 2, "life": 2, "amount": 8},
            },
            "hard": {
                "ship": {"velocity": 1, "life": 3},
                "pawns": {"velocity": 1, "life": 1, "amount": 14},
                "knights": {"velocity": 1, "life": 2, "amount": 12},
                "bishops": {"velocity": 2, "life": 2, "amount": 10},
            },
            "insane": {
                "ship": {"velocity": 2, "life": 5},
                "pawns": {"velocity": -1, "life": 2, "amount": 16},
                "knights": {"velocity": -1, "life": 2, "amount": 14},
                "bishops": {"velocity": 1, "life": 2, "amount": 12},
            },
        }

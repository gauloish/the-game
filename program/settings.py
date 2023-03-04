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
        self.step = 5

        self.back = [230, 230, 230]

        self.display = "The Game"

        self.amounts = {
            "easy": {
                "back": {"rate": 14},
                "ship": {"velocity": 3, "life": 1},
                "pawns": {"velocity": 4, "life": 1, "amount": 10},
                "knights": {"velocity": 3, "life": 1, "amount": 8},
                "bishops": {"velocity": 2, "life": 1, "amount": 6},
            },
            "medium": {
                "back": {"rate": 12},
                "ship": {"velocity": 5, "life": 1},
                "pawns": {"velocity": 6, "life": 1, "amount": 12},
                "knights": {"velocity": 5, "life": 1, "amount": 10},
                "bishops": {"velocity": 4, "life": 2, "amount": 8},
            },
            "hard": {
                "back": {"rate": 10},
                "ship": {"velocity": 7, "life": 3},
                "pawns": {"velocity": 8, "life": 1, "amount": 14},
                "knights": {"velocity": 7, "life": 2, "amount": 12},
                "bishops": {"velocity": 6, "life": 2, "amount": 10},
            },
            "insane": {
                "back": {"rate": 8},
                "ship": {"velocity": 9, "life": 5},
                "pawns": {"velocity": 10, "life": 2, "amount": 16},
                "knights": {"velocity": 9, "life": 2, "amount": 14},
                "bishops": {"velocity": 8, "life": 2, "amount": 12},
            },
        }

from tile import Tile


class Level:
    """
    Part of Map class
    Level represents current screen on which the character is located
    Contains tiles and transitions to other levels of the map
    """

    def __init__(self, w, h):
        self.width = w
        self.height = h

        self.map: list[list[Tile]]
        self.transitions: dict[Tile: Level] = {}

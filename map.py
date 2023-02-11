from level import Level


class Map:
    def __init__(
            self,
            levels: list[Level]
    ):
        self.levels: list[Level] = levels
        self.player_level: Level


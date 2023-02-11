from tile import Tile


class Entity:
    def __init__(
            self,
            walkable: bool,
            tile: Tile
    ):
        self.walkable: bool = walkable
        self.x = 0
        self.y = 0
        self.pos = (self.x, self.y)
        self.tile: Tile = tile


class Player(Entity):
    def __init__(self, tile):
        super().__init__(False, tile)

from entity import Entity


class Tile:
    """
    Part of Level class, located at certain position
    A container for terrain and object
    """

    def __init__(self, terrain, entities: list[Entity]):
        self.terrain = terrain
        self.entities: list[Entity] = entities

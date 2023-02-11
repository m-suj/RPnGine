class Tile:
    """
    Part of Level class, located at certain position
    A container for terrain and object
    """

    def __init__(self, terrain, entity):
        self.terrain = terrain
        self.entity = entity

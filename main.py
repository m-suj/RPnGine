import arcade
from stg import game_window
from map import Map
from level import Level
from tile import Tile
from entity import Entity, Player


tile_map = [Tile() for i in range(10) [Tile() for j in range(10)]]

levels = [
    Level(10, 10, tile_map),
    Level(10, 10, tile_map)
]

map = Map(levels)

player = Player(map.levels[0].map[0][0])


class Game(arcade.Window):
    def __init__(self):
        super().__init__(game_window.w, game_window.h, game_window.title)

        self.map = worldmap
        self.player = player

        arcade.set_background_color(arcade.color.WHITE_SMOKE)

    def setup(self):
        pass

    def on_update(self, dt: float):
        pass

    def on_draw(self):
        self.clear()

    def on_key_press(self, key, keymod):
        if key == arcade.key.ESCAPE:
            arcade.exit()

    def on_key_release(self, key, keymod):
        pass


def main():
    """ Main function """
    game = Game()
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()

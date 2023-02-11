import arcade
from stg import game_window


class Game(arcade.Window):
    def __init__(self):
        super().__init__(game_window.w, game_window.h, game_window.title)

        arcade.set_background_color(arcade.color.AMAZON)

    # def setup(self):

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

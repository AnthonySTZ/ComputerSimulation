from game_renderer import Renderer
from input import Input


if __name__ == "__main__":

    game = Renderer(800)
    game.init_window()
    game.run()

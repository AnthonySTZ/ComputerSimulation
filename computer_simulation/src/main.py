from game_renderer import Renderer
from input import Input
from output import Output


if __name__ == "__main__":

    game = Renderer(800)
    game.init_window()
    input = Input((200, 200))
    output = Output((300, 200))
    input.connect_to(output, 0, 0)  # Connect the input item to the output item
    game.add_item(input)  # Add an input item to the game
    game.add_item(output)  # Add an input item to the game
    game.run()

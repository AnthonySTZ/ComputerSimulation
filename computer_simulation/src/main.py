from game_renderer import Renderer
from input import Input
from output import Output
from gates import AndGate

if __name__ == "__main__":

    game = Renderer(800)
    game.init_window()
    input = Input((200, 200))
    input_2 = Input((200, 300))
    and_gate = AndGate((300, 250))
    output = Output((400, 250))
    input.connect_to(and_gate, 0, 0)  # Connect the input item to the AND gate
    input_2.connect_to(and_gate, 0, 1)  # Connect the input item to the AND gate
    and_gate.connect_to(output, 0, 0)  # Connect the AND gate output to the output item
    game.add_item(input)  # Add an input item to the game
    game.add_item(input_2)  # Add an input item to the game
    game.add_item(and_gate)  # Add an AND gate to the game
    game.add_item(output)  # Add an input item to the game

    game.run()

from game_renderer import Renderer
from input import Input
from output import Output
from gates import AndGate, OrGate, XorGate, BinToIntGate
import pygame as pg


def create_default_full_adder(
    game_renderer,
) -> None:  # Create a simple adder for testing purposes
    input_A = Input((200, 200))
    input_B = Input((200, 300))
    input_C = Input((200, 400))

    xor_gate_1 = XorGate((300, 250))
    xor_gate_2 = XorGate((400, 300))

    and_gate_1 = AndGate((400, 400))
    and_gate_2 = AndGate((400, 500))

    or_gate_1 = OrGate((500, 425))

    output_1 = Output((600, 350))
    output_2 = Output((600, 425))

    bin_to_int_gate = BinToIntGate((700, 375))

    input_A.connect_to(xor_gate_1, 0, 0)
    input_A.connect_to(and_gate_2, 0, 0)
    input_B.connect_to(xor_gate_1, 0, 1)
    input_B.connect_to(and_gate_2, 0, 1)
    input_C.connect_to(xor_gate_2, 0, 1)
    input_C.connect_to(and_gate_1, 0, 1)

    xor_gate_1.connect_to(xor_gate_2, 0, 0)
    xor_gate_1.connect_to(and_gate_1, 0, 0)
    xor_gate_2.connect_to(output_1, 0, 0)

    and_gate_1.connect_to(or_gate_1, 0, 0)
    and_gate_2.connect_to(or_gate_1, 0, 1)

    or_gate_1.connect_to(output_2, 0, 0)

    output_1.connect_to(bin_to_int_gate, 0, 3)
    output_2.connect_to(bin_to_int_gate, 0, 2)

    game.add_item(input_A)
    game.add_item(input_B)
    game.add_item(input_C)

    game.add_item(xor_gate_1)
    game.add_item(xor_gate_2)

    game.add_item(and_gate_1)
    game.add_item(and_gate_2)

    game.add_item(or_gate_1)

    game.add_item(output_1)
    game.add_item(output_2)

    game.add_item(bin_to_int_gate)


if __name__ == "__main__":

    game = Renderer(1200)
    game.init_window()

    create_default_full_adder(game)

    game.run()

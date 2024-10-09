from game_renderer import Renderer
from input import Input
from output import Output
from gates import AndGate, OrGate
import pygame as pg

if __name__ == "__main__":

    game = Renderer(1200)
    game.init_window()
    input = Input((200, 200))
    input_2 = Input((200, 300))
    input_3 = Input((200, 400))
    and_gate = AndGate((300, 250))
    output = Output((400, 250))

    or_gate = OrGate((300, 350))

    game.add_item(input)  # Add an input item to the game
    game.add_item(input_2)  # Add an input item to the game
    game.add_item(input_3)  # Add an input item to the game
    game.add_item(and_gate)  # Add an AND gate to the game
    game.add_item(output)  # Add an input item to the game
    game.add_item(or_gate)  # Add an OR gate to the game

    game.run()

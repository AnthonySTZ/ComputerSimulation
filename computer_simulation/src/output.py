from item import Item
import pygame as pg


class Output(Item):
    def __init__(self, position=(0, 0)) -> None:
        super().__init__("OUT", (155, 155, 155), position, 1, 1)
        self.state = True

    def get_output_value(self, connection_index) -> bool:
        if self.inputs[0] is None:
            return False

        input_node = self.inputs[0][0]
        input_connection_index = self.inputs[0][1]

        return input_node.get_output_value(input_connection_index)

    def clicked(self):
        pass

    def update(self) -> None:
        self.color = (100, 200, 100) if self.get_output_value(0) else (155, 155, 155)

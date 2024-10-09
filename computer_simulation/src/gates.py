from item import Item
import pygame as pg


class AndGate(Item):
    def __init__(self, position=(0, 0)) -> None:
        super().__init__("AND", (200, 200, 50), position, 2, 1)
        self.state = True

    def get_output_value(self, connection_index) -> bool:
        if self.inputs[0] is None or self.inputs[1] is None:
            return False

        input_node_1 = self.inputs[0][0]
        input_connection_index_1 = self.inputs[0][1]

        input_node_2 = self.inputs[1][0]
        input_connection_index_2 = self.inputs[1][1]

        return input_node_1.get_output_value(
            input_connection_index_1
        ) and input_node_2.get_output_value(input_connection_index_2)

    def clicked(self):
        pass

    def update(self) -> None:
        pass


class OrGate(Item):
    def __init__(self, position=(0, 0)) -> None:
        super().__init__(
            "OR",
            (
                50,
                200,
                200,
            ),
            position,
            2,
            1,
        )
        self.state = True

    def get_output_value(self, connection_index) -> bool:
        if self.inputs[0] is None or self.inputs[1] is None:
            return False

        input_node_1 = self.inputs[0][0]
        input_connection_index_1 = self.inputs[0][1]

        input_node_2 = self.inputs[1][0]
        input_connection_index_2 = self.inputs[1][1]

        return input_node_1.get_output_value(
            input_connection_index_1
        ) or input_node_2.get_output_value(input_connection_index_2)

    def clicked(self):
        pass

    def update(self) -> None:
        pass

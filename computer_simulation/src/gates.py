from item import Item
import pygame as pg


class AndGate(Item):
    def __init__(self, position=(0, 0)) -> None:
        super().__init__(position, 2, 1)
        self.state = True
        self.color = (200, 200, 50)

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

    def draw(self, screen) -> None:
        rect = pg.Rect(
            self.position[0],
            self.position[1],
            self.size[0],
            self.size[1],
        )

        pg.draw.rect(screen, pg.Color(self.color), rect)

        self.draw_connections(screen)


class OrGate(Item):
    def __init__(self, position=(0, 0)) -> None:
        super().__init__(position, 2, 1)
        self.state = True
        self.color = (50, 200, 200)

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

    def draw(self, screen) -> None:
        rect = pg.Rect(
            self.position[0],
            self.position[1],
            self.size[0],
            self.size[1],
        )

        pg.draw.rect(screen, pg.Color(self.color), rect)

        self.draw_connections(screen)

from item import Item
import pygame as pg


class Output(Item):
    def __init__(self, position=(0, 0)) -> None:
        super().__init__(position, 1, 1)
        self.state = True
        self.color = (155, 155, 155)

    def get_output_value(self, connection_index) -> bool:
        if self.inputs[connection_index] is None:
            return False

        input_node = self.inputs[connection_index][0]
        input_connection_index = self.inputs[connection_index][1]

        return input_node.get_output_value(input_connection_index)

    def clicked(self):
        pass

    def update(self) -> None:
        self.color = (100, 200, 100) if self.get_output_value(0) else (155, 155, 155)

    def draw(self, screen) -> None:
        rect = pg.Rect(
            self.position[0],
            self.position[1],
            self.size[0],
            self.size[1],
        )

        pg.draw.rect(screen, pg.Color(self.color), rect)

        self.draw_connections(screen)

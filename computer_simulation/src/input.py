from item import Item
import pygame as pg
import logics


class Input(Item):
    def __init__(self, position=(0, 0)) -> None:
        super().__init__(position)
        self.number_of_inputs = 0
        self.number_of_outputs = 1
        self.state = False
        self.color = (200, 0, 0)

    def get_output_node(self) -> Item | None:
        return None

    def get_output_value(self, connection_index) -> bool:
        return self.state

    def clicked(self):
        self.state = not self.state
        self.change_color()

    def change_color(self) -> None:
        self.color = (0, 200, 0) if self.state else (200, 0, 0)

    def get_rect(self) -> pg.Rect:
        rect = pg.Rect(
            self.position[0],
            self.position[1],
            self.size[0],
            self.size[1],
        )

        return rect

    def is_mouse_over(self, mouse_position: tuple) -> bool:
        return logics.check_collision(
            self.position, self.size[0], self.size[1], mouse_position
        )

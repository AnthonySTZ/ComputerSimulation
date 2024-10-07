from item import Item
import pygame as pg


class Input(Item):
    def __init__(self) -> None:
        super().__init__()
        self.number_of_inputs = 0
        self.number_of_outputs = 1
        self.state = False
        self.color = (200, 0, 0)

    def get_output_node(self) -> Item | None:
        return None

    def get_output_value(self, connection_index) -> bool:
        return self.state

    def toogle_state(self):
        self.state = not self.state
        self.change_color()

    def change_color(self) -> None:
        self.color = (0, 200, 0) if self.state else (200, 0, 0)

    def get_rect(self) -> pg.Rect:
        rect = pg.Rect(
            self.position[0],
            self.position[1],
            20,
            20,
        )

        return rect

    def is_mouse_over(self, mouse_position: tuple) -> bool:
        rect = self.get_rect()
        return rect.collidepoint(mouse_position)

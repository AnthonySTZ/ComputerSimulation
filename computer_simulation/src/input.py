from item import Item
import pygame as pg


class Input(Item):
    def __init__(self, position=(0, 0)) -> None:
        super().__init__("IN", (200, 0, 0), position, 0, 1)
        self.state = False

    def get_output_node(self) -> Item | None:
        return None

    def get_output_value(self, connection_index) -> bool:
        return self.state

    def clicked(self):
        self.state = not self.state

    def update(self) -> None:
        self.color = (0, 200, 0) if self.state else (200, 0, 0)

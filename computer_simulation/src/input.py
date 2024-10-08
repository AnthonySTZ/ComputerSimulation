from item import Item
import pygame as pg


class Input(Item):
    def __init__(self, position=(0, 0)) -> None:
        super().__init__(position, 0, 1)
        self.state = False
        self.color = (200, 0, 0)

    def get_output_node(self) -> Item | None:
        return None

    def get_output_value(self, connection_index) -> bool:
        return self.state

    def clicked(self):
        self.state = not self.state

    def update(self) -> None:
        self.color = (0, 200, 0) if self.state else (200, 0, 0)

    def draw(self, screen) -> None:
        rect = pg.Rect(
            self.position[0],
            self.position[1],
            self.size[0],
            self.size[1],
        )

        pg.draw.rect(screen, pg.Color(self.color), rect)

        for output in self.outputs.values():
            line_start_pos = (
                self.position[0] + self.size[0] / 2,
                self.position[1] + self.size[1] / 2,
            )
            line_end_pos = (
                output[0].position[0] + output[0].size[0] / 2,
                output[0].position[1] + output[0].size[1] / 2,
            )
            pg.draw.line(
                screen,
                pg.Color(10, 10, 10),
                line_start_pos,
                line_end_pos,
            )

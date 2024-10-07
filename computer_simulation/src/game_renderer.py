import pygame as pg
from input import Input


class Renderer:
    def __init__(self, window_width=600) -> None:

        self.window_size = (window_width, window_width * 0.7)
        self.items = []

    def init_window(self) -> None:
        pg.init()
        pg.display.set_caption("Computer Simulation")
        self.screen = pg.display.set_mode(self.window_size)

    def run(self) -> None:
        run = True
        while run:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                elif event.type == pg.MOUSEBUTTONUP:
                    pos = pg.mouse.get_pos()
                    for item in self.items:
                        if item.is_mouse_over(pos):
                            item.toogle_state()

            self.screen.fill(pg.Color(210, 210, 210))

            self.draw_items()

            pg.display.flip()

        pg.quit()

    def add_item(self, item) -> None:
        self.items.append(item)

    def draw_items(self) -> None:
        for item in self.items:
            pg.draw.rect(self.screen, pg.Color(item.color), item.get_rect())

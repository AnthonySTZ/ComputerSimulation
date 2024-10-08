import pygame as pg
from input import Input
from output import Output
from item import Item


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
        mouse_down = False
        curr_item_selected = None
        prev_mouse = (0, 0)
        mouse_motion = 0
        mouse_motion_threshold = 10
        while run:
            mouse_pos = pg.mouse.get_pos()
            mouse_motion += abs(mouse_pos[0] - prev_mouse[0]) + abs(
                mouse_pos[1] - prev_mouse[1]
            )
            prev_mouse = mouse_pos
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                if event.type == pg.MOUSEBUTTONUP:
                    if mouse_motion < mouse_motion_threshold:
                        item = self.get_item_under_mouse(mouse_pos)
                        if item is not None:
                            item.clicked()
                    mouse_down = False
                    curr_item_selected = None

                elif event.type == pg.MOUSEBUTTONDOWN:
                    mouse_motion = 0
                    mouse_down = True
                    curr_item_selected = self.get_item_under_mouse(mouse_pos)

                if mouse_down:
                    if mouse_motion >= mouse_motion_threshold:
                        if curr_item_selected is not None:
                            curr_item_selected.drag(mouse_pos)

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_i:
                        print("Item Input created")
                        self.add_item(Input(mouse_pos))

                    if event.key == pg.K_o:
                        print("Item Output created")
                        self.add_item(Output(mouse_pos))

            self.screen.fill(pg.Color(210, 210, 210))

            self.draw_items()

            pg.display.flip()

        pg.quit()

    def add_item(self, item) -> None:
        self.items.append(item)

    def draw_items(self) -> None:
        for item in self.items:
            item.update()
            item.draw(self.screen)

    def get_item_under_mouse(self, pos) -> Item | None:
        for item in self.items:
            if item.is_mouse_over(pos):
                return item
        return None

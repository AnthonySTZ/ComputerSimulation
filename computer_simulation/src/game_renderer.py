import pygame as pg


class Renderer:
    def __init__(self, window_width=600) -> None:

        self.window_size = (window_width, window_width * 0.8)

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

        pg.quit()

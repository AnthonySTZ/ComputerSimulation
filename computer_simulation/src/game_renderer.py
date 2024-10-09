import pygame as pg
from input import Input
from output import Output
from item import Item
from gates import AndGate, OrGate


class Renderer:
    def __init__(self, window_width=600) -> None:

        self.window_size = (window_width, window_width * 0.7)
        self.items = []

    def init_window(self) -> None:
        pg.init()
        pg.font.init()
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

            # Check if mouse over input or output
            for item in self.items:
                mouse_over_slot_index = item.set_mouse_over_slots(mouse_pos)
                if mouse_over_slot_index is not None:
                    break

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                if event.type == pg.MOUSEBUTTONUP:
                    if mouse_motion < mouse_motion_threshold:
                        if mouse_over_slot_index is not None:
                            item: Item = mouse_over_slot_index[0]
                            slot_type: str = mouse_over_slot_index[1]
                            slot_index: int = mouse_over_slot_index[2]
                            print(
                                f"Mouse over slot : {slot_type} num°{slot_index} of item {item}"
                            )
                            if slot_type == "input":
                                if item.inputs[slot_index] is not None:
                                    input_connections = [
                                        i for i in item.inputs[slot_index]
                                    ]
                                    conn_item: Item = input_connections[0]
                                    conn_index: int = input_connections[1]
                                    conn_item.unconnect_from(
                                        item, conn_index, slot_index
                                    )
                        else:
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

                    if event.key == pg.K_r:
                        print("Item OR created")
                        self.add_item(OrGate(mouse_pos))

                    if event.key == pg.K_a:
                        print("Item AND created")
                        self.add_item(AndGate(mouse_pos))

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

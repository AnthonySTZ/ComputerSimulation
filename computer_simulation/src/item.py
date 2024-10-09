from abc import ABC, abstractmethod
import logics
import pygame as pg


class Item:
    def __init__(self, position=(0, 0), nb_inputs=0, nb_outputs=0) -> None:

        self.position = position
        self.size = (50, 50)
        self.number_of_inputs = nb_inputs
        self.number_of_outputs = nb_outputs
        self.input_over = None
        self.output_over = None
        self.slot_size = 10
        self.inputs = {i: None for i in range(nb_inputs)}
        self.outputs = {i: {} for i in range(nb_outputs)}

    def drag(self, position: tuple) -> None:
        self.position = (position[0] - self.size[0] / 2, position[1] - self.size[1] / 2)

    def is_mouse_over(self, mouse_position: tuple) -> bool:
        return logics.check_collision(
            self.position, self.size[0], self.size[1], mouse_position
        )

    def set_mouse_over_slots(self, position: tuple) -> None:
        for i in range(self.number_of_inputs):
            input_corner_position = (
                self.position[0] - self.slot_size / 2,
                self.position[1]
                + (i + 1) / (self.number_of_inputs + 1) * self.size[1]
                - self.slot_size / 2,
            )
            if logics.check_collision(
                input_corner_position, self.slot_size, self.slot_size, position
            ):
                self.input_over = i
                return
        self.input_over = None

        for i in range(self.number_of_outputs):
            output_corner_position = (
                self.position[0] - self.slot_size / 2 + self.size[0],
                self.position[1]
                + (i + 1) / (self.number_of_outputs + 1) * self.size[1]
                - self.slot_size / 2,
            )
            if logics.check_collision(
                output_corner_position, self.slot_size, self.slot_size, position
            ):
                self.output_over = i
                return
        self.output_over = None

    def connect_to(
        self, connection, first_connection_index: int, second_connection_index: int
    ) -> None:
        self.outputs[first_connection_index][connection] = second_connection_index
        connection.inputs[second_connection_index] = [self, first_connection_index]

    def draw_inputs_and_outputs_slots(self, screen) -> None:

        for i in range(self.number_of_inputs):
            if self.input_over == i:
                slot_color = pg.Color(155, 0, 0)
            else:
                slot_color = pg.Color(50, 50, 50)
            pg.draw.rect(
                screen,
                slot_color,
                (
                    self.position[0] - self.slot_size / 2,
                    self.position[1]
                    + (i + 1) / (self.number_of_inputs + 1) * self.size[1]
                    - self.slot_size / 2,
                    self.slot_size,
                    self.slot_size,
                ),
            )

        for i in range(self.number_of_outputs):
            if self.output_over == i:
                slot_color = pg.Color(155, 0, 0)
            else:
                slot_color = pg.Color(50, 50, 50)
            pg.draw.rect(
                screen,
                slot_color,
                (
                    self.position[0] - self.slot_size / 2 + self.size[0],
                    self.position[1]
                    + (i + 1) / (self.number_of_outputs + 1) * self.size[1]
                    - self.slot_size / 2,
                    self.slot_size,
                    self.slot_size,
                ),
            )

    def draw_connections(self, screen) -> None:

        self.draw_inputs_and_outputs_slots(screen)

        for start_output_index, outputs in self.outputs.items():
            for output, end_input_index in outputs.items():

                line_start_pos = (
                    self.position[0] + self.size[0],
                    self.position[1]
                    + (start_output_index + 1)
                    / (self.number_of_outputs + 1)
                    * self.size[1],
                )
                line_end_pos = (
                    output.position[0],
                    output.position[1]
                    + (end_input_index + 1)
                    / (output.number_of_inputs + 1)
                    * output.size[1],
                )
                pg.draw.aaline(
                    screen,
                    pg.Color(10, 10, 10),
                    line_start_pos,
                    line_end_pos,
                )

    @abstractmethod
    def clicled(self) -> None:
        pass

    @abstractmethod
    def update(self) -> None:
        pass

    @abstractmethod
    def draw(self) -> None:
        pass

from abc import ABC, abstractmethod
import logics


class Item:
    def __init__(self, position=(0, 0), nb_inputs=0, nb_outputs=0) -> None:

        self.position = position
        self.size = (30, 30)
        self.number_of_inputs = nb_inputs
        self.number_of_outputs = nb_outputs
        self.inputs = {}
        self.outputs = {}

    def drag(self, position: tuple) -> None:
        self.position = (position[0] - self.size[0] / 2, position[1] - self.size[1] / 2)

    def is_mouse_over(self, mouse_position: tuple) -> bool:
        return logics.check_collision(
            self.position, self.size[0], self.size[1], mouse_position
        )

    def connect_to(
        self, connection, first_connection_index: int, second_connection_index: int
    ) -> None:
        self.outputs[first_connection_index] = [connection, second_connection_index]
        connection.inputs[second_connection_index] = [self, first_connection_index]

    @abstractmethod
    def clicled(self) -> None:
        pass

    @abstractmethod
    def update(self) -> None:
        pass

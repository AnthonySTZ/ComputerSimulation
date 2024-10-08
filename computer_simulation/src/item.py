from abc import ABC, abstractmethod


class Item:
    def __init__(self) -> None:

        self.position = (0, 0)
        self.size = (30, 30)
        self.number_of_inputs = 0
        self.number_of_outputs = 0
        self.inputs = []
        self.outputs = []

    def drag(self, position: tuple) -> None:
        self.position = (position[0] - self.size[0] / 2, position[1] - self.size[1] / 2)

    @abstractmethod
    def clicled(self) -> None:
        pass

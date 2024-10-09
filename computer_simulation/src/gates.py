from item import Item
import pygame as pg
import logics


class AndGate(Item):
    def __init__(self, position=(0, 0)) -> None:
        super().__init__("AND", (200, 200, 50), position, 2, 1)

    def get_output_value(self, connection_index) -> bool:
        values = [False for _ in range(self.number_of_inputs)]
        for i in range(self.number_of_inputs):
            if self.inputs[i] is not None:
                values[i] = self.inputs[i][0].get_output_value(self.inputs[i][1])

        return values[0] and values[1]

    def clicked(self):
        pass

    def update(self) -> None:
        pass


class OrGate(Item):
    def __init__(self, position=(0, 0)) -> None:
        super().__init__(
            "OR",
            (
                50,
                200,
                200,
            ),
            position,
            2,
            1,
        )

    def get_output_value(self, connection_index) -> bool:
        values = [False for _ in range(self.number_of_inputs)]
        for i in range(self.number_of_inputs):
            if self.inputs[i] is not None:
                values[i] = self.inputs[i][0].get_output_value(self.inputs[i][1])

        return values[0] or values[1]

    def clicked(self):
        pass

    def update(self) -> None:
        pass


class NotGate(Item):
    def __init__(self, position=(0, 0)) -> None:
        super().__init__(
            "NOT",
            (
                50,
                200,
                50,
            ),
            position,
            1,
            1,
        )

    def get_output_value(self, connection_index) -> bool:
        values = [False for _ in range(self.number_of_inputs)]
        for i in range(self.number_of_inputs):
            if self.inputs[i] is not None:
                values[i] = self.inputs[i][0].get_output_value(self.inputs[i][1])

        return not values[0]

    def clicked(self):
        pass

    def update(self) -> None:
        pass


class NandGate(Item):
    def __init__(self, position=(0, 0)) -> None:
        super().__init__(
            "NAND",
            (
                20,
                200,
                80,
            ),
            position,
            2,
            1,
        )

    def get_output_value(self, connection_index) -> bool:
        values = [False for _ in range(self.number_of_inputs)]
        for i in range(self.number_of_inputs):
            if self.inputs[i] is not None:
                values[i] = self.inputs[i][0].get_output_value(self.inputs[i][1])

        return not (values[0] and values[1])

    def clicked(self):
        pass

    def update(self) -> None:
        pass


class NorGate(Item):
    def __init__(self, position=(0, 0)) -> None:
        super().__init__(
            "NOR",
            (
                200,
                20,
                80,
            ),
            position,
            2,
            1,
        )

    def get_output_value(self, connection_index) -> bool:
        values = [False for _ in range(self.number_of_inputs)]
        for i in range(self.number_of_inputs):
            if self.inputs[i] is not None:
                values[i] = self.inputs[i][0].get_output_value(self.inputs[i][1])

        return not (values[0] or values[1])

    def clicked(self):
        pass

    def update(self) -> None:
        pass


class XorGate(Item):
    def __init__(self, position=(0, 0)) -> None:
        super().__init__(
            "XOR",
            (
                200,
                250,
                20,
            ),
            position,
            2,
            1,
        )

    def get_output_value(self, connection_index) -> bool:
        values = [False for _ in range(self.number_of_inputs)]
        for i in range(self.number_of_inputs):
            if self.inputs[i] is not None:
                values[i] = self.inputs[i][0].get_output_value(self.inputs[i][1])

        return (values[0] or values[1]) and (not values[0] or not values[1])

    def clicked(self):
        pass

    def update(self) -> None:
        pass


class BinToIntGate(Item):
    def __init__(self, position=(0, 0)) -> None:
        super().__init__(
            "0",
            (
                30,
                250,
                60,
            ),
            position,
            4,
            0,
            (50, 75),
        )

    def get_output_value(self, connection_index) -> bool:
        pass

    def clicked(self):
        pass

    def update(self) -> None:
        values = ["0" for _ in range(self.number_of_inputs)]
        for i in range(self.number_of_inputs):
            if self.inputs[i] is not None:
                values[i] = str(
                    int(self.inputs[i][0].get_output_value(self.inputs[i][1]))
                )

        bin_to_int = logics.binaries_to_integer("".join(values))
        self.text = str(bin_to_int)

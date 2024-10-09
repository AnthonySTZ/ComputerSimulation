from item import Item
import pygame as pg


class AndGate(Item):
    def __init__(self, position=(0, 0)) -> None:
        super().__init__("AND", (200, 200, 50), position, 2, 1)

    def get_output_value(self, connection_index) -> bool:
        val_1 = False
        val_2 = False

        if self.inputs[0] is not None:
            val_1 = self.inputs[0][0].get_output_value(self.inputs[0][1])

        if self.inputs[1] is not None:
            val_2 = self.inputs[1][0].get_output_value(self.inputs[1][1])

        return val_1 and val_2

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
        val_1 = False
        val_2 = False

        if self.inputs[0] is not None:
            val_1 = self.inputs[0][0].get_output_value(self.inputs[0][1])

        if self.inputs[1] is not None:
            val_2 = self.inputs[1][0].get_output_value(self.inputs[1][1])

        return val_1 or val_2

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
        val_1 = False

        if self.inputs[0] is not None:
            val_1 = self.inputs[0][0].get_output_value(self.inputs[0][1])

        return not val_1

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
        val_1 = False
        val_2 = False

        if self.inputs[0] is not None:
            val_1 = self.inputs[0][0].get_output_value(self.inputs[0][1])

        if self.inputs[1] is not None:
            val_2 = self.inputs[1][0].get_output_value(self.inputs[1][1])

        return not (val_1 and val_2)

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
        val_1 = False
        val_2 = False

        if self.inputs[0] is not None:
            val_1 = self.inputs[0][0].get_output_value(self.inputs[0][1])

        if self.inputs[1] is not None:
            val_2 = self.inputs[1][0].get_output_value(self.inputs[1][1])

        return not (val_1 or val_2)

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
        val_1 = False
        val_2 = False

        if self.inputs[0] is not None:
            val_1 = self.inputs[0][0].get_output_value(self.inputs[0][1])

        if self.inputs[1] is not None:
            val_2 = self.inputs[1][0].get_output_value(self.inputs[1][1])

        return (val_1 or val_2) and (not val_1 or not val_2)

    def clicked(self):
        pass

    def update(self) -> None:
        pass

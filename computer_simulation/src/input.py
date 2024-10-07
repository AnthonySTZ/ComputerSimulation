from item import Item


class Input(Item):
    def __init__(self) -> None:
        super().__init__()
        self.number_of_inputs = 0
        self.number_of_outputs = 1
        self.state = False
        self.color = (200, 0, 0)

    def get_output_node(self) -> Item | None:
        return None

    def get_output_value(self, connection_index) -> bool:
        return self.state

    def toogle_state(self) -> bool:
        self.state = not self.state
        return self.state

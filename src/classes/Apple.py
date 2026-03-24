from src.classes.BoxElement import BoxElement


class Apple(BoxElement):
    def __init__(self, x_pos, y_pos):
        super().__init__('#a70000', x_pos, y_pos)

    def update(self):
        pass

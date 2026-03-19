from src.classes.BoxElement import BoxElement


class Tail(BoxElement):
    def __init__(self, x_pos, y_pos):
        super().__init__('#6b946c', x_pos, y_pos)

    def set_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass

from src.classes.BoxElement import BoxElement


class Apple(BoxElement):
    def __init__(self):
        super().__init__('#a70000', 60, 100)

    def update(self):
        pass

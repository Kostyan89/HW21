class Hero:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_position(self):
        return self.x, self.y

    def set_position(self, x, y):
        self.x = x
        self.y = y


field = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

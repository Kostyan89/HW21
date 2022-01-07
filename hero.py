class Unit:
    def __init__(self, hp, got_key, coord, escaped):
        self.hp = hp
        self.got_key = got_key
        self.coord = coord
        self.escaped = escaped


class Ghost(Unit):
    def __init__(self, name, hp, got_key, coord, escaped):
        super().__init__(hp, got_key, coord, escaped)
        self.name = name

    def get_coordinates(self):
        pass

    def set_coordinates(self, x, y):
        pass

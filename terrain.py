class Terrain():

    def __init__(self, terrain, walkable):
        self.terrain = terrain
        self.walkable = walkable

    def is_walkable(self):
        return self.walkable

    def get_terrain(self):
        return self.terrain


class Grass(Terrain):
    def __init__(self):
        super().__init__(terrain="grass", walkable=True)


class Wall(Terrain):
    def __init__(self):
        super().__init__(terrain="wall", walkable=False)


class Door(Terrain):
    def __init__(self):
        super().__init__(terrain="door", walkable=True)


class Key(Terrain):
    def __init__(self):
        super().__init__(terrain="key", walkable=True)


class Trap(Terrain):
    def __init__(self):
        super().__init__(terrain="trap", walkable=True)
        
class Terrain:

    def __init__(self, terrain, walkable):
        self.terrain = terrain
        self.walkable = walkable

    def is_walkable(self):
        return self.walkable

    def get_terrain(self):
        return self.terrain


class Grass(Terrain):
    def __init__(self):
        super().__init__(terrain="Grass", walkable=True)


class Wall(Terrain):
    def __init__(self):
        super().__init__(terrain="Wall", walkable=False)


class Door(Terrain):
    def __init__(self):
        super().__init__(terrain="Door", walkable=False)

    def step_on(self, unit):
        if unit.has_key():
            self.walkable = True


class Key(Terrain):
    def __init__(self):
        super().__init__(terrain="Key", walkable=True)

    def get_key(self, unit):
        if not unit.got_key:
            unit.got_key = True


class Trap(Terrain):
    def __init__(self, damage):
        super().__init__(terrain="Trap", walkable=True)
        self.damage = damage

    def step_on(self, unit):
        unit.get_damage(damage=self.damage)

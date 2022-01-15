from model.hero import Unit


class Terrain:

    def __init__(self, terrain, walkable):
        self.terrain = terrain
        self.walkable = walkable

    def is_walkable(self):
        return self.walkable

    def get_terrain(self):
        return self.terrain

    def step_on(self, unit):
        pass


class Grass(Terrain):
    def __init__(self):
        super().__init__(terrain="Grass", walkable=True)


class Wall(Terrain):
    def __init__(self):
        super().__init__(terrain="Wall", walkable=False)


class Door(Terrain):
    def __init__(self):
        super().__init__(terrain="Door", walkable=True)

    def step_on(self, unit: Unit):
        if unit.got_key:
            unit.escaped = True
        else:
            print('Нужен ключ, чтобы выйти')


class Key(Terrain):
    def __init__(self):
        super().__init__(terrain="Key", walkable=True)

    def step_on(self, unit):
        unit.got_key = True


class Trap(Terrain):
    def __init__(self, damage):
        super().__init__(terrain="Trap", walkable=True)
        self.damage = damage

    def step_on(self, unit):
        unit.get_damage(damage=self.damage)

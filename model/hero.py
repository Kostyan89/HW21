from exeptions import UnitDied


class Unit:
    def __init__(self, hp, got_key, coord, escaped, defense):
        self.hp = hp
        self.got_key = False
        self.coord = coord
        self.escaped = False
        self.defense = defense

    def get_coordinates(self):
        """возвращает координаты юнита"""
        return self.coord

    def set_coordinates(self, x, y):
        "устанавливает координат юнита"
        self.coord = (x, y)

    def has_key(self):
        """проверяет, есть ли у данного юнита ключ."""
        if not self.got_key:
            return True

    def set_key(self):
        """ставит маркер got_key в True."""
        self.got_key = True

    def has_escaped(self):
        """проверяет, удалось ли сбежать."""
        if not self.escaped:
            return True

    def is_alive(self):
        """проверяет, есть ли еще у юнита положительное количество хит-поинтов."""
        if self.hp <= 0:
            raise UnitDied
        return True

    def get_damage(self, damage):
        """обрабатывает входящий урон с учетом текущего параметра защиты.
        Если юнит умирает после атаки, должно быть выброшено исключение UnitDied."""
        if damage > self.defense:
            self.hp = self.hp - (damage - self.defense)
        self.is_alive()

    def has_position(self, x, y):
        """проверяет в этих ли координатах установлен юнит"""
        return self.coord[0] == x and self.coord[1] == y


class Ghost(Unit):
    def __init__(self, name, hp, got_key, coord, escaped, defense):
        super().__init__(hp, got_key, coord, escaped, defense)
        self.name = name

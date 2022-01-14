from exeptions import UnitDied


class Unit:
    def __init__(self, hp, coord: tuple, defense):
        self.hp = hp
        self.got_key = False
        self.coord = coord
        self.escaped = False
        self.defense = defense

    def get_coordinates(self):
        """Возвращает координаты юнита"""
        return self.coord

    def set_coordinates(self, x, y):
        "Устанавливает координат юнита"
        self.coord = (x, y)

    def has_key(self):
        """Проверяет, есть ли у данного юнита ключ."""
        return self.got_key


    def set_key(self):
        """Ставит маркер got_key в True."""
        self.got_key = True

    def has_escaped(self):
        """Проверяет, удалось ли сбежать."""
        return self.escaped


    def is_alive(self):
        """Проверяет, есть ли еще у юнита положительное количество хит-поинтов."""
        if self.hp <= 0:
            raise UnitDied
        return True

    def get_damage(self, damage):
        """Обрабатывает входящий урон с учетом текущего параметра защиты.
        Если юнит умирает после атаки, должно быть выброшено исключение UnitDied."""
        if damage > self.defense:
            self.hp = self.hp - (damage - self.defense)
        self.is_alive()

    def has_position(self, x, y):
        """Проверяет в этих ли координатах установлен юнит"""
        return self.coord == (x, y)


class Ghost(Unit):
    def __init__(self,hp, coord, defense):
        super().__init__(hp, coord, defense)
        self.name = Ghost

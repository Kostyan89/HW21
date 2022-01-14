from typing import List

import config
from model.hero import Unit
from model.terrain import Wall, Grass, Key, Door, Trap


class Cell:
    def __init__(self, obj):
        self.obj = obj

    def get_object(self):
        return self.obj

    def set_object(self, obj):
        self.obj = obj


class Field:
    def __init__(self, string_field: str, unit: Unit):

        self.unit = unit
        self.play_field = self.fill_area(string_field)
        self.cols = len(self.play_field[0])
        self.rows = len(self.play_field)

    def get_cell(self, x, y) -> Cell:
        """Метод, возвращающий объект находящийся по данным координатам"""
        return self.play_field[y][x]

    def movement(self, direction):
        """Направление и кол-во шагов юнита"""
        (x, y) = self.unit.get_coordinates()
        if direction == "w":
            x += 1
        elif direction == "s":
            x -= 1
        elif direction == "a":
            y -= 1
        elif direction == "d":
            y += 1
        else:
            print("Указано неправильное направление. Используйте пожалуйста команды: w, a, s, d")
        self.unit.set_coordinates(x, y)
        return x, y

    def move_te_cell(self, x, y):
        """Если поле проходимое, меняет координаты героя"""
        if self.get_cell(x, y).get_object().walkable:
            self.unit.set_coordinates(x, y)
        else:
            print("Проход закрыт")

    def get_field(self):
        """Возвращает свойство field."""
        return self.play_field

    def get_cols(self):
        """Возвращает кол-во столбцов в поле"""
        return self.cols

    def get_rows(self):
        """Возвращает кол-во строк в поле"""
        return self.rows

    def fill_area(self, string_field: str) -> List[List[Cell]]:
        """Заполняет ячейки игрового поля"""
        area = []
        for line in string_field.split("\n"):
            line = line.strip()
            cell_list = []
            for item in line:
                cell_list.append(self._choose_cell(item))
            area.append(cell_list)
        return area

    def _choose_cell(self, letter: str) -> Cell:
        """Определяет ячейки для заполнения игрового поля"""
        data = {
            "W": Wall,
            "g": Grass,
            "K": Key,
            "D": Door,
            "T": Trap
        }
        if letter == "G":
            return Cell(self.unit)
        elif letter == "T":
            return Cell(Trap(damage=config.trap_damage))
        else:
            return Cell(data[letter]())






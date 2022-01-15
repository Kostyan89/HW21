from typing import List, Union

import config
from model.hero import Unit
from model.terrain import Terrain, Wall, Grass, Key, Door, Trap


class Cell:
    def __init__(self, obj: Union[Terrain, Unit]):
        self.obj = obj

    def get_object(self):
        return self.obj

    def set_object(self, obj):
        self.obj = obj

    def __repr__(self):
        return self.obj.__class__.__name__


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
        x, y = self.unit.get_coordinates()
        if direction == "w":
            x -= 1
        elif direction == "s":
            x += 1
        elif direction == "a":
            y -= 1
        elif direction == "d":
            y += 1
        else:
            assert False, 'До сюда дойти цикл не должен, т.к. проверка есть в ui.py'

        target_field = self.play_field[x][y].get_object()
        if isinstance(target_field, Terrain):
            if not target_field.walkable:
                print("Проход закрыт")
            else:
                target_field.step_on(self.unit)
                self.unit.set_coordinates(x, y)

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

    @staticmethod
    def _choose_cell(letter: str) -> Cell:
        """Определяет ячейки для заполнения игрового поля"""
        data = {
            "W": Wall,
            "g": Grass,
            "K": Key,
            "D": Door,
            "T": Trap
        }
        if letter == "T":
            return Cell(data[letter](damage=config.trap_damage))
        elif letter in data:
            return Cell(data[letter]())
        else:
            assert False, f'Can not mapping {letter}'






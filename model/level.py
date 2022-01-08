from model.hero import Ghost


class Cell:
    def __init__(self, obj):
        self.obj = obj

    def get_object(self):
        return self.obj

    def set_object(self, obj):
        self.obj = obj


class Field:
    def __init__(self, field, cols, rows, unit):

        self.field = field
        self.unit = unit
        self.cols = cols
        self.rows = rows

    def get_cell(self, x, y):
        """метод, возвращающий объект находящийся по данным координатам"""
        return self.field[x][y]

    def move_unit(self, direction, steps: int):
        """направление и кол-во шагов юнита"""
        x, y = self.unit.get_coordinates()
        if direction == "w":
            x += steps
        elif direction == "s":
            x -= steps
        elif direction == "a":
            y -= steps
        elif direction == "d":
            y += steps
        else:
            print("указано неправильное направление. Используйте пожалуйста команды: w, a, s, d")
        self.unit.set_coordinates()

    def get_field(self):
        """возвращает свойство field."""
        return self.field

    def get_cols(self):
        """возвращает кол-во столбцов в поле"""
        return self.cols

    def get_rows(self):
        """возвращает кол-во строк в поле"""
        return self.rows

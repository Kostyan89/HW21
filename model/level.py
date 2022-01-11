from model.hero import Unit


class Cell:
    def __init__(self, obj):
        self.obj = obj

    def get_object(self):
        return self.obj

    def set_object(self, obj):
        self.obj = obj


class Field:
    def __init__(self, field, cols, rows, unit: Unit):

        self.field = field
        self.unit = unit
        self.cols = cols
        self.rows = rows

    def get_cell(self, x, y):
        """Метод, возвращающий объект находящийся по данным координатам"""
        return self.field[x][y]

    def move_unit(self, direction):
        """Направление и кол-во шагов юнита"""
        x, y = self.unit.get_coordinates()
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
        self.unit.set_coordinates(self.get_cell(y, x)[0], self.get_cell(y, x)[1])

    def get_field(self):
        """Возвращает свойство field."""
        return self.field

    def get_cols(self):
        """Возвращает кол-во столбцов в поле"""
        return self.cols

    def get_rows(self):
        """Возвращает кол-во строк в поле"""
        return self.rows

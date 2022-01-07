class Cell:
    def __init__(self, obj):
        self.obj = obj

    def get_object(self):
        return self.obj

    def set_object(self, obj):
        self.obj = obj


class Field:
    def __init__(self, field, unit, cols, rows):

        self.field = field
        self.unit = unit
        self.cols = cols
        self.rows = rows

    def get_cell(self, x, y):
        pass

    def move_unit_up(self):
        pass

    def move_unit_down(self):
        pass

    def move_unit_right(self):
        pass

    def move_unit_left(self):
        pass

    def get_field(self):
        pass

    def get_cols(self):
        pass

    def get_rows(self):
        pass


import config
from model.level import Cell, Field
from model.hero import Ghost, Unit
from model.terrain import Grass, Wall, Door, Key, Trap


class Hero:
    pass


class GameController:
    def __init__(self, string_field, unit: Unit):
        self.mapping = config.mapping
        self.game_on = True
        self.unit = unit
        self.field = Field(string_field, unit)

    def _draw_field(self):
        graphic = []
        for y in range(self.field.get_rows()):
            items_list = []
            for x in range(self.field.get_cols()):
                cell_type = self.field.get_cell(x, y).get_object().__class__
                image = self.mapping[cell_type]
                items_list.append(image)
            graphic.append("".join(items_list))
        print("\n".join(graphic))

    def play(self):
        while self.game_on and not self.unit.has_escaped():
            self._draw_field()
            direction = input()
            if direction in ["w", "s", "d", "a"]:
                self.unit_move(self.field.movement(direction)[0], self.field.movement(direction)[1])
            elif direction in ["stop", "exit"]:
                self.game_on = False
                print("Конец игры")
            else:
                print("Вы ввели неправильную команду")

    def unit_move(self, x, y):
        if self.field.get_cell(y, x).get_object().get_terrain() == Trap:
            self.field.move_te_cell(x=x, y=y)
            self.unit.get_damage(Trap(self.unit).step_on(config.trap_damage))
            print("Ловушка! Вы получаете урон")
        elif self.field.get_cell(y, x).get_object().get_terrain() == Key:
            print('Получен ключ')
            self.field.move_te_cell(x=x, y=y)
            self.unit.set_key()
        elif self.field.get_cell(y, x).get_object().get_terrain() == Door and self.unit.got_key():
            self.field.move_te_cell(x=x, y=y)
            print("Победа")
            self.unit.has_escaped()
        elif self.field.get_cell(y, x).get_object().get_terrain() == Grass:
            self.field.move_te_cell(x=x, y=y)


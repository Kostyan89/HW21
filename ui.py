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
        self.hero = unit
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
        while self.game_on and not self.hero.has_escaped():
            self._draw_field()
            direction = input()
            if direction in ["w", "s", "d", "a"]:
                self.field.unit_move(self.field.movement(direction)[0], self.field.movement(direction)[1])
            elif direction in ["stop", "exit"]:
                self.game_on = False
                print("Конец игры")
            else:
                print("Вы ввели неправильную команду")

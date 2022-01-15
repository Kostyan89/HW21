import config
from model.hero import Ghost, Unit
from model.level import Field
from pprint import pprint

from model.terrain import Grass, Key


class GameController:
    def __init__(self, string_field, unit: Unit):
        self.mapping = config.mapping
        self.game_on = True
        self.unit = unit
        self.field = Field(string_field, unit)
        pprint(self.field.play_field)

    def _draw_field(self):
        graphic = []
        for y in range(self.field.get_rows()):
            items_list = []
            for x in range(self.field.get_cols()):
                cell_type = self.field.get_cell(x, y).get_object().__class__
                if self.unit.has_position(y, x):
                    cell_type = Ghost
                elif self.unit.got_key and cell_type == Key:
                    cell_type = Grass
                items_list.append(self.mapping[cell_type])
            graphic.append("".join(items_list))
        print("\n".join(graphic))

    def play(self):
        while self.game_on and not self.unit.has_escaped():
            self._draw_field()
            direction = input().lower()
            if direction in ["w", "s", "d", "a"]:
                self.field.movement(direction)
            elif direction in ["stop", "exit"]:
                self.game_on = False
                print("Конец игры")
            else:
                print("Вы ввели неправильную команду")

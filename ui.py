import config
from model.level import Cell, Field
from model.hero import Ghost, Unit
from model.terrain import Grass, Wall, Door, Key, Trap


class Hero:
    pass


class GameController:
    def __init__(self):
        self.mapping = config.mapping
        self.game_on = True
        self.hero = Unit
        self.field = None

    def make_field(self):
        fields = []
        with open('labyrinth.txt', 'r') as f:
            arr = f.readlines()
        row = len(arr[0])
        col = len(arr)
        unit = Unit(hp=50, coord=(row, col), defense=1)
        for line_n, line in enumerate(arr):
            field_line = []
            for item_n, item in enumerate(line.strip("\n")):
                if item == "W":
                    field_line.append(Cell(Wall()))
                if item == "g":
                    field_line.append(Cell(Grass()))
                if item == "G":
                    field_line.append(Unit)
                if item == "K":
                    field_line.append(Cell(Key()))
                if item == "D":
                    field_line.append(Cell(Door()))
                if item == "T":
                    field_line.append(Cell(Trap(damage=config.trap_damage)))
            fields.append(field_line)
            self.field = Field(fields, col, row, unit)

    def play(self):
        self.make_field()
        self._draw_field()
        while self.game_on and not self.hero.has_escaped:
            direction = input("Куда направитесь?")
            if direction in ["w", "s", "d", "a"]:
                self.field.move(direction)
            elif direction in ["stop", "exit"]:
                self.game_on = False
            elif self.hero.has_escaped:
                break
            else:
                print("Вы ввели неправильную команду")

    def _draw_field(self):
        for y, line in enumerate(self.field.get_field()):
            s = ""
            for x, item in enumerate(line):
                if self.hero.get_coordinates():
                    s += self.mapping["ghost"]
                else:
                    s += self.mapping[item.get_object().get_terrain()]
            print(s)

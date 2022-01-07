import config
from field import Cell, Field
from hero import Ghost
from terrain import Grass, Wall, Door, Key, Trap


class Hero:
    pass


class GameController:
    def __init__(self):
        self.mapping = config.mapping
        self.game_on = True
        self.hero = None
        self.field = None

    def make_field(self, lvlstrng):
        fields = []
        with open('game_field.txt', 'r') as f:
            arr = f.readlines()
        row = len(arr[0])
        col = len(arr)
        for line_n, line in enumerate(arr):
            field_line = []
            for item_n, item in enumerate(line.strip("\n")):
                if item == "W":
                    field_line.append(Cell(Wall()))
                if item == "g":
                    field_line.append(Cell(Grass()))
                if item == "G":
                    field_line.append(Cell(Grass()))
                    self.hero = Ghost(item_n, line_n, item_n)
                if item == "K":
                    field_line.append(Cell(Key()))
                if item == "D":
                    field_line.append(Cell(Door()))
                if item == "T":
                    field_line.append(Cell(Trap()))
            fields.append(field_line)
            self.field = Field(fields, col, row, self.hero)

    def play(self,  name, hp, got_key, coord, escaped, defense):

        self.hero = Ghost(name, hp, got_key, coord, escaped, defense)
        while self.game_on and not self.hero.escaped:
            command = input()
            if command == "w":
                self.field.move_unit_up()
            elif command == "s":
                self.field.move_unit_down()
            elif command == "a":
                self.field.move_unit_left()
            elif command == "d":
                self.field.move_unit_right()
            elif command in ["stop", "exit"]:
                self.game_on = False
            elif self.hero.escaped:
                break

    def _draw_field(self):
        for cell in self.field:
            print(cell)

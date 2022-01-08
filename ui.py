import config
from model.level import Cell, Field
from model.hero import Ghost
from model.terrain import Grass, Wall, Door, Key, Trap


class Hero:
    pass


class GameController:
    def __init__(self):
        self.mapping = config.mapping
        self.game_on = True
        self.hero = Ghost
        self.field = None

    def make_field(self):
        fields = []
        with open('labyrinth.txt', 'r') as f:
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
                    field_line.append(Ghost)
                if item == "K":
                    field_line.append(Cell(Key()))
                if item == "D":
                    field_line.append(Cell(Door()))
                if item == "T":
                    field_line.append(Cell(Trap(damage=config.trap_damage)))
            fields.append(field_line)
            self.field = Field(fields, col, row, self.hero)

    def play(self):
        self.make_field()
        while self.game_on and not self.hero.has_escaped:
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
            elif self.hero.has_escaped:
                break
            else:
                print("Вы ввели неправильную команду")

    def _draw_field(self):
        for cell in self.field:
            print(cell)

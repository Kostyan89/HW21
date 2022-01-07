import config
from field import Cell
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
        cell_1 = Cell(Wall())
        cell_2 = Cell(Grass())
        cell_3 = Cell(Grass())

        field = [
            [cell_1, cell_2, cell_3]
        ]

    self.field = Field()
    self.field.set_field(field)

    def play(self):

        self.hero = Hero(...)
        while self.game_on and not hero.escaped:
            command = input()
            if command == "w":
                self.field.move_unit_up()
            elif command == "s":
                self.field.move_unit_down()
            elif command == "a":
                self.field.move_unit_left()
            elif command == "d":
                self.field.move_unit_right()
            elif command == "stop":
                self.game_on = False
            elif hero.escaped == True:
                break

    def _draw_field(self):
        for cell in self.field:
            print(cell)

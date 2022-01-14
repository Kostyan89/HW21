from model.hero import Ghost
from ui import GameController


def read_file() -> str:
    with open('labyrinth.txt', 'r') as f:
        return "".join(f.readlines())


gc = GameController(string_field=read_file(), unit=Ghost(hp=50, coord=(2, 2), defense=1))

gc.play()

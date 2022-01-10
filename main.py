from model.hero import Ghost
from ui import GameController

gc = GameController(Ghost(hp=50, coord=(2,2), defense=1))

gc.play()

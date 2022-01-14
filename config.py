from model.hero import Ghost
from model.terrain import Wall, Grass, Key, Door, Trap

mapping = {
		Wall: '🔲',
		Grass: '⬜',
		Ghost: '👻',
		Key: '🗝',
		Door: '🚪',
		Trap: '💀',
	}

trap_damage = 3

default_hp = 10

default_coordinates = 0, 0

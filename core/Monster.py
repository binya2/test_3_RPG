from enum import Enum

from core.Entity import Entity


class Monster_type(Enum):
    Orc = "Orc"
    Goblin = "Goblin"


class Weapon(Enum):
    Knife = 0
    Sword = 1
    Axe = 2


class Monster(Entity):
    def __init__(self, name: str, hp: int, speed: int, power: int, armor_rating: int,
                 monster_type: Monster_type,weapon: Weapon) -> None:
        super().__init__(name, hp, speed, power, armor_rating)
        self.monster_type: Monster_type = monster_type
        self.weapon: Weapon = weapon

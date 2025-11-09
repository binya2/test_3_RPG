from enum import Enum

from core.Entity_player import Entity_player, roll_dice


class Monster_type(Enum):
    Orc = 0
    Goblin = 1


class Weapon(Enum):
    Knife = 0
    Sword = 1
    Axe = 2


class Monster(Entity_player):
    def __init__(self, name: str, hp: int, speed: int, power: int, armor_rating: int,
                 monster_type: Monster_type, weapon: Weapon) -> None:
        super().__init__(name, hp, speed, power, armor_rating)
        self.monster_type: Monster_type = monster_type
        self.weapon: Weapon = weapon

    def damage(self, sides:int) -> int:
        damage_mul = 1
        if self.weapon == Weapon.Knife:
            damage_mul = 0.5
        if self.weapon == Weapon.Axe:
            damage_mul = 2
        damage = (roll_dice(sides) + self.power) * damage_mul
        return damage

    def __str__(self) -> str:
        super_str:str = super().__str__()
        return super_str + f", Weapon: {self.weapon.__str__().replace('.',': ')}"

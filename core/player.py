import random
from enum import Enum

from core.Entity_player import Entity_player, roll_dice


class Profession(Enum):
    Healer = 0
    Warrior = 1


class Player(Entity_player):
    def __init__(self, name: str) -> None:
        random_number = random.randrange
        name: str = name
        hp: int = 50
        speed = random_number(5, 10)
        power = random_number(5, 10)
        armor_rating = random_number(5, 15)
        super().__init__(name, hp, speed, power, armor_rating)
        self.profession: Profession = Profession(random_number(1, 10) % 2)

    def speak(self):
        print(f"Hi, my name is '{self.name}'!! ")

    def damage(self)-> int:
        return roll_dice(6) + self.power

    def __str__(self) -> str:
        super_str:str = super().__str__()
        return super_str + f", Profession: {self.profession.__str__().replace('.',': ')}"
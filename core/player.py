import random
from enum import Enum

from core.Entity import Entity


class Profession(Enum):
    Healer = 0
    Warrior = 1

class Player(Entity):
    def __init__(self, name:str  )->None:
        random_number = random.randrange
        name:str = name
        hp:int = 50
        speed = random_number(5,10)
        power = random_number(5,10)
        armor_rating = random_number(5, 15)

        super().__init__(name, hp ,speed, power, armor_rating)

        self.profession : Profession = Profession(random_number(1,10) % 2)

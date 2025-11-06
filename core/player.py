import random
from enum import Enum


class Profession(Enum):
    Healer = 0
    Warrior = 1

class Player:
    def __init__(self, name:str  )->None:
        random_number = random.randrange
        self.name:str = name
        self.hp:int = 50
        self.speed = random_number(5,10)
        self.power = random_number(5,10)
        self.armor_rating = random_number(5,15)
        self.profession : Profession = Profession(random_number(1,10) % 2)

    def speak(self):
        print(f"Hi, my name is '{self.name}'")

    def attack(self):
        pass
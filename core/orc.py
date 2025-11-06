import random

from core.Monster import Monster, Monster_type, Weapon


class Orc(Monster):
    def __init__(self, name: str) -> None:
        random_number = random.randrange
        hp: int = 50
        speed = random_number(0, 5)
        power = random_number(10, 15)
        armor_rating = random_number(2, 8)
        weapon = Weapon(random_number(0, 10) % 3)
        super().__init__(name, hp, speed, power, armor_rating, Monster_type.Orc, weapon)

    def speak(self) -> None:
        print(f"The {self.name} Bob is angry!")

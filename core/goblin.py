import random

from core.Monster import Monster, Monster_type, Weapon


class Goblin(Monster):
    def __init__(self, name: str) -> None:
        random_number = random.randrange
        name: str = name
        hp: int = 20
        speed = random_number(5, 10)
        power = random_number(5, 10)
        armor_rating = 1
        weapon = Weapon(random_number(0, 10) % 3)
        super().__init__(name, hp, speed, power, armor_rating, Monster_type.Goblin, weapon)

    def speak(self) -> None:
        print(f"Goblin {self.name} is furious!")

    def run_away(self) -> None:
        pass

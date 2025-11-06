import random


def roll_dice(sides) -> int:
    return random.randrange(0, sides)


class Entity_player(object):
    def __init__(self, name: str, hp: int, speed: int, power: int, armor_rating: int) -> None:
        self.name: str = name
        self.hp: int = hp
        self.speed: int = speed
        self.power: int = power
        self.armor_rating: int = armor_rating

    def speak(self):
        pass

    def attack(self, other):
        attack_planning: int = self.damage()
        if attack_planning > other.armor_rating:
            print(f"{self.name} Attacking {other.name}\n"
                  f"The damage is: {attack_planning}")
            other.hp -= attack_planning
        return other.status_check()

    def status_check(self):
        return self.hp <= 0

    def damage(self) -> int:
        pass

    def __str__(self) -> str:
           return f"Name: {self.name} - Life: {self.hp}, Speed: {self.speed}, Power: {self.power}, Armor Rating: {self.armor_rating}"
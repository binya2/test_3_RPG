class Entity(object):
    def __init__(self, name: str, hp: int, speed: int, power: int, armor_rating: int) -> None:
        self.name = name
        self.hp = hp
        self.speed = speed
        self.power = power
        self.armor_rating = armor_rating

    def speak(self):
        print(f"Hi, my name is '{self.name}'")

    def attack(self):
        pass

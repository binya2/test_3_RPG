import random

from core.Entity_player import roll_dice
from core.Monster import Monster, Monster_type
from core.goblin import Goblin
from core.orc import Orc
from core.player import Player


class Game:
    def __init__(self):
        self.Attacker = self.create_player()
        self.Attacked = self.choose_random_monster()

    def start(self):
        print(f"Welcome to the battle!!!")
        self.Attacker.speak()
        self.Attacked.speak()
        self.choose_the_first_one()
        self.battle()

    def show_menu(self):
        print(f"\nPlayers status:\n"
              f"{self.Attacked.__str__()} \n"
              f"{self.Attacker.__str__()}\n"
              f"Current attacker: {self.Attacked.name} \n")
        return input("If you are interested in a fight, press B, otherwise press Q: ").upper()

    def create_player(self):
        return Player("Gandalf the White")

    def choose_random_monster(self) -> Monster:
        monster_type: Monster_type = Monster_type(random.randrange(0, 10) % 2)
        if monster_type == Monster_type.Orc:
            return Orc("Azog")
        return Goblin("Joe")

    def battle(self):
        user_input = self.show_menu()
        while user_input != 'Q':
            attacked_is_dead = self.Attacker.attack(self.Attacked)
            if attacked_is_dead:
                break
            self.Attacked, self.Attacker = self.Attacker, self.Attacked
            user_input = self.show_menu()

    def choose_the_first_one(self):
        Attacker_roll = self.roll_dice(6) + self.Attacker.speed
        Attacked_roll = self.roll_dice(6) + self.Attacked.speed
        if Attacker_roll < Attacked_roll:
            self.Attacked, self.Attacker = self.Attacker, self.Attacked

    def roll_dice(self, sides) -> int:
        return roll_dice(sides)
        # return random.randrange(0, sides)

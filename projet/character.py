from dice import Dice

# SOLID
    # S
    # D


class Character:
    def __init__(self, name, hp_max, attack_value, defense_value, dice) -> None:
        self.name = name
        self.hp_max = hp_max
        self.hp = hp_max
        self.attack_value = attack_value
        self.defense_value = defense_value
        self.dice = dice

    def __str__(self) -> str:
        return f"""I'm {self.name}. Those are my caracs :
    - {self.hp}/{self.hp_max} hp
    - att: {self.attack_value}
    - def: {self.defense_value}"""

    def is_alive(self):
        return self.hp > 0

    def decrease_hp(self, amount):
        self.hp = self.hp - amount
        if self.hp < 0:
            self.hp = 0
        self.show_healthbar()

    def increase_hp(self, amount):
        self.hp += amount

    def show_healthbar(self):
        print(
            f"[{'o' * self.hp}{' ' * (self.hp_max - self.hp)}] {self.hp}/{self.hp_max}hp"
        )

    def compute_damages(self):
        return self.attack_value + self.dice.roll()

    def attack(self, target):
        if self.is_alive():
            damages = self.compute_damages()
            print(
                f"{self.name} attack with {damages} (att: {self.attack_value} + roll: {damages - self.attack_value})"
            )
            target.defense(damages)

    def defense(self, damages):
        print(f"damages: {damages}")
        roll = self.dice.roll()
        raw_damages = damages - self.defense_value - roll
        print(
            f"{self.name} defend againt {damages} and took {raw_damages} damages ({damages} - def: {self.defense_value} - roll: {roll})"
        )
        self.decrease_hp(raw_damages)


class Warrior(Character):

    def compute_damages(self):
        return super().compute_damages() + 3
    
class Mage(Character):
    # Bonus de +3 à la défense
    pass


char1 = Warrior("James", 20, 8, 3, Dice("red", 6))
char2 = Warrior("Lisa", 20, 8, 3, Dice("blue", 6))

while char1.is_alive() and char2.is_alive():
    char1.attack(char2)
    char2.attack(char1)

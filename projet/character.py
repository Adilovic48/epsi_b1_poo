from dice import Dice


class Character:
    def __init__(self, name, hp_max, attack_value, defense_value) -> None:
        self.name = name
        self.hp_max = hp_max
        self.hp = hp_max
        self.attack_value = attack_value
        self.defense_value = defense_value

    def __str__(self) -> str:
        return f"""I'm {self.name}. Those are my caracs :
    - {self.hp}/{self.hp_max} hp
    - att: {self.attack_value}
    - def: {self.defense_value}"""
    
    def is_alive(self):
        return self.hp > 0

    def decrease_hp(self, amount):
        self.hp -= amount

    def increase_hp(self, amount):
        self.hp += amount

    def show_healthbar(self):
        print(f"[{"o" * self.hp}{" " * (self.hp_max - self.hp)}] {self.hp}/{self.hp_max}hp")

    def attack(self):
        a_dice = Dice("red", 6)
        damages = self.attack_value + a_dice.roll()
        print(f"{self.name} attack with {damages} (att: {self.attack_value} + roll: {damages - self.attack_value})")
        return damages
    
    def defense(self, damages):
        a_dice = Dice("red", 6)
        roll = a_dice.roll()
        raw_damages = damages - self.defense_value - roll
        print(f"{self.name} defend againt {damages} and took {raw_damages} damages ({damages} - def: {self.defense_value} - roll: {roll})")
        return raw_damages

char1 = Character("James", 20, 8, 3)
char2 = Character("Lisa", 20, 8, 3)
# print(char1)

dmg = char2.attack()
dmg = char2.defense(dmg)
char2.decrease_hp(dmg)
char2.show_healthbar()

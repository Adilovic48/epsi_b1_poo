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
        self.hp = self.hp - amount

    def increase_hp(self, amount):
        self.hp = self.hp + amount

    def show_healthbar(self):
        print(f"[{"o" * self.hp}{" " * (self.hp_max - self.hp)}] {self.hp}/{self.hp_max}hp")

# char1 = Character("James", 20, 8, 3)
# print(char1)

char2 = Character("Lisa", 20, 8, 3)
char2.decrease_hp(8)
char2.decrease_hp(6)
char2.show_healthbar()

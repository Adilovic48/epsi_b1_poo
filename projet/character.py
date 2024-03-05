from dice import Dice


class Character:
    def __init__(self, name, hp_max, attack_value, defense_value) -> None:
        self.name = name
        self.hp_max = hp_max
        self.attack_value = attack_value
        self.defense_value = defense_value

    def __str__(self) -> str:
        return f"I'm {self.name} (att: {self.attack_value} / def: {self.defense_value})"
    

    # is_alive
        # retourne un booléen
    
    # show_healthbar
        # affiche une barre de vie sous la forme:
        # [oooooo            ] 6/12hp

char1 = Character("James", 20, 8, 3)
char2 = Character("Lisa", 20, 8, 3)

print(char1)
print(char2)
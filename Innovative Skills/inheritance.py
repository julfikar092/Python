class game_character:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def damageHealth(self, amount):
        self.health -= amount
        print(f"{self.name} takes {amount} damage! health is now {self.health}")


class wizard(game_character):
    def cast_spell(self):
        print(f"{self.name} cast fireball")


class warrior(game_character):
    def swing_sord(self):
        print(f"{self.name} swings heavy sword!")


Omen = wizard("Omen")
Kartos = warrior("Kartos")

Omen.cast_spell()
Kartos.damageHealth(20)

Kartos.swing_sord()
Omen.damageHealth(15)

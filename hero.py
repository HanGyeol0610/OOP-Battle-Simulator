import random

class Hero:
    """The hero blueprint will be implemented later in the project."""

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 25

    def attack(self):
        totalAttack = 0
        totalAttack=random.randint(1, self.attack_power)
        if random.randint(1,3) == 1:
            totalAttack = totalAttack + (totalAttack // 3)
            print("Crit hit of: " + str(totalAttack // 3))
        return totalAttack
    
    def take_damage(self, damage):
        self.health = max(0, self.health - damage)
        print(f"{self.name} takes {damage} damage. Health: {self.health}")
    
    def is_alive(self):
        return self.health > 0
    
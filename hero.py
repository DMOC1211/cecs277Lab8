'''
Name: Jacob Miranda & Daniel Puerto
Date: 03/10/26
Group: 13
Description:
'''

import random
from entity import Entity 

class Hero(Entity.Entity):
    def __init__(self, name, max_hp):
        super().__init__(name, max_hp)

    def sword_attack(self, dragon):
        # Sword attack that damages the dragon and returns a string
        damage = random.randint(1, 6) + random.randint(1, 6)
        dragon.take_damage(damage)
        return f"{self.name} attacks {dragon.name} with a sword for {damage} damage!"
    
    def arrow_attack(self, dragon):
        # Arrow attack that damages the dragon and returns a string
        damage = random.randint(10, 80)
        dragon.take_damage(damage)
        return f"{self.name} attacks {dragon.name} with an arrow for {damage} damage!"

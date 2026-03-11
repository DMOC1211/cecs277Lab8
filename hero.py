'''
Name: Jacob Miranda & Daniel Puerto
Date: 03/10/26
Group: 13
Description:
'''

import random
from entity import Entity 

class Hero(Entity):
    
    def sword_attack(self, dragon):
        damage = random.randint(1, 6) + random.randint(1, 6)
        dragon.take_damage(damage)
        return f"{self.name} attacks {dragon.name} with a sword for {damage} damage!"
    
    def arrow_attack(self, dragon):
        damage = random.randint(1, 12)
        dragon.take_damage(damage)
        return f"{self.name} attacks {dragon.name} with an arrow for {damage} damage!"

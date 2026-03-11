'''
Name: Jacob Miranda & Daniel Puerto
Date: 03/10/26
Group: 13
Description:
'''
import random
import Entity

class Dragon(Entity.Entity):
    def __init__(self, name, max_hp):
        super().__init__(name, max_hp)
        

    def basic_attack(self, hero):
        damage = random.randint(2, 5)
        hero.take_damage(damage)
        return f"{self.name} attacks {hero.name} for {damage} damage!"

    def special_attack(self, hero):
        damage = random.randint(3, 7)
        hero.take_damage(damage)
        return f"{self.name} uses a special attack on {hero.name} for {damage} damage!"

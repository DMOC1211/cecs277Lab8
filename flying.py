'''
Name: Jacob Miranda & Daniel Puerto
Date: 03/10/26
Group: 13
Description: A flying dragon that deals damage only using their swoops, and it's damage depends
on whether or not they have any swoops remaining
'''
import random 
import dragon

class FlyingDragon(dragon.Dragon):
# A dragon that can swoop a limited number of times
    def __init__(self, name, hp):
    # Initializes FlyingDragon with a name, HP and swoop count, flying dragon starts with 2 swoops
        super().__init__(name, hp)
        self._swoops = 2

    def special_attack(self, hero):
    # Swoop attack deals 5-9 damage, but only if swoops remain, if there are no swoops remaining, it deals 0 damage and prints a message
        if self._swoops > 0:
            dmg = random.randint(5,9)
            hero.take_damage(dmg)
            self._swoops -= 1
            return f"{self.name} swoops down on {hero.name} for {dmg} damage!"
        else:
            return f"{self.name} tries to swoop but has no swoops left!"

    def __str__(self):
        # Return dragon's name, HP and remaining swoops
        return f"{self._name}: {self.hp}/{self.max_hp} HP (Swoops: {self._swoops})"

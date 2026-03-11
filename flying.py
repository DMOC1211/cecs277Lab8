'''
Name: Jacob Miranda & Daniel Puerto
Date: 03/10/26
Group: 13
Description:
'''
import random 
from dragon Import Dragon

class FlyingDragon(Dragon):

  def __init__(self,name, hp):

    super().__init__(name, hp)
    self._swoops = 2

  def special_attack(self, hero):

    if self._swoops > 0:
      dmg = random.randint(5,9)
      hero.take_damage(dmg)
      self._swoops -= 1
      return f"{self.name} swoops down on {hero.name} folr {dmg} damage!"
    else:
      return f"{self.name} tries to swoop but has no swoops left!"

  def __str__(self):

    return f"{self.name}: {self.hp} HP (Swoops: {self._swoops})"

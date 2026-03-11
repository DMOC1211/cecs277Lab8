'''
Name: Jacob Miranda & Daniel Puerto
Date: 03/10/26
Group: 13
Description:
'''

import random 
from dragon import Dragon

class FireDragon(Dragon):
# A dragon that can breathe fire a limited number of times
  def __init__(self,name, hp):
      # Initializes a Fire Dragon with a name, HP and fire shot count. Fire dragons start with 3 fire shots 
    super().__init__(name,hp)
    self._fire_shots = 3

  def special_attack(self, hero):
    #Fire breath attack deals 4-8 damage only if fire shots remain, if no shots remain, it deals 0 damage and prints a message.
    if self._fire_shots > 0:
      dmg = random.randint(4,8)
      hero.take_damage(dmg)
      self._fire_shots -= 1
      return f"{self.name} breathes fire at {hero.name} for {dmg} damage!"
    else:
      return f"{self.name} tries to breathe fire, but has no fire shots left!"


  def __str__(self):
    #Shows dragon's name, HP and the remaining fire shots
    return f"{self.name}: {self.hp} HP (Fire shots: {self._fire_shots})"

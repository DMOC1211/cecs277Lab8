'''
Name: Jacob Miranda & Daniel Puerto
Date: 03/10/26
Group: 13
Description:
'''

class Entity():
    
  #Represents an Entity with a name and hit points (HP)
    def __init__(self, name, max_hp):
        # Initializes an Entity with a name and max HP starting at max_hp
        self._name = name
        self._max_hp = max_hp
        self._hp = max_hp

    @property
    def name(self):
        #Return the entitys name
        return self._name

    @property
    def hp(self):
    #returns the entitys current HP
        return self._hp

    def take_damage(self, dmg):
        #Reduces the HP by the dmg, HP can't go below 0
        self._hp -= dmg
        if self._hp < 0:
            self._hp = 0

    def __str__(self):
        #Returns a string in the format: Name: hp/max_hp
        return f"{self._name}: {self._hp}/{self._max_hp}"
    

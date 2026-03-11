'''
Name: Jacob Miranda & Daniel Puerto
Date: 03/10/26
Group: 13
Description:
'''

import Entity
import Hero
import Dragon
import check_input
import random

def main():
    player = Hero.Hero("Player", 100)
    dragon = Dragon.Dragon("Dragon", 150)
    print(player)
    print(dragon) 
    print()

    print("Pick an attack:")
    print("1. Sword Attack")
    print("2. Arrow Attack")
    choice = check_input.get_int_range("Enter your choice (1 or 2): ", 1, 2)

    if choice == 1:
        print(player.sword_attack(dragon))
    elif choice == 2:
        print(player.arrow_attack(dragon))

    print(dragon)
    print()

    choice_dragon = random.randint(1, 2)
    if choice_dragon == 1:
        print(dragon.basic_attack(player))
    elif choice_dragon == 2:
        print(dragon.special_attack(player))
    print(player)

main()

'''
Name: Jacob Miranda & Daniel Puerto
Date: 03/10/26
Group: 13
Description: Creates and loops how and when the hero interacts with the dragons and how/when the dragons interact with the hero.
Establishes the hero's name and hp and dragon's name and hp. Allows for the hero to pick which attack to hit which dragon.  
When a dragon dies the count drops and the damage the hero recieves drops, the game ends when either the hero dies or all the dragons do.
'''

import hero
import dragon
import fire
import flying
import check_input
import random

def main():
    name = input("Enter your hero's name: ")

    player = hero.Hero(name, 50)
    basic_dragon = dragon.Dragon("Dragon", 30)
    fire_dragon = fire.FireDragon("Fire Dragon", 40)
    flying_dragon = flying.FlyingDragon("Flying Dragon", 25)
    dragons=[basic_dragon, fire_dragon, flying_dragon]
    while True:
        print(player)
        print("Dragons:")
        for d in dragons:
            print(d)
        choice = check_input.get_int_range("Choose a dragon to attack: ", 1, len(dragons))
        dragon1= dragons[choice - 1]

        print("Pick an attack:")
        print("1. Sword Attack")
        print("2. Arrow Attack")
        choice = check_input.get_int_range("Enter your choice (1 or 2): ", 1, 2)

        if choice == 1:
            print(player.sword_attack(dragon1))
        elif choice == 2:
            print(player.arrow_attack(dragon1))
        for d in dragons:
            if d.hp <= 0:
                print(f"{d.name} has been defeated!")
                dragons.remove(d)
        print()

        if len(dragons) == 0:
            print("Congratulations! You have defeated all the dragons!")
            break
        
        try:
            attacker = random.choice(dragons)
        except IndexError:
            print("All dragons have been defeated!")
            break

        choice_dragon = random.randint(1, 2)
        if choice_dragon == 1:
            print(attacker.basic_attack(player))
        elif choice_dragon == 2:
            print(attacker.special_attack(player))
        print()

        if player.hp <= 0:
            print("You have been defeated by the dragons. Game over.")
            break


main()

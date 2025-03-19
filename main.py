import random 
import os
from player import Player
from enemy import Enemy
from food import Food
from drinks import Drinks

player = Player(10, 10, 0, 3) # Health, Hydration, Gold, Damage
enemy = Enemy(10, 5, 3) # Health, Gold, Damage
meet = Food("meet", 5)
water = Drinks("water", 3)

player_choise = int(input("1. Eat: \n2. Drink: \n3. Fight: \n4.  \nwhat do you want to do: "))

if player_choise == 1:
  player.health += meet.regenerate_food

if player_choise == 2:
  player.hydration += water.regenerate_hydration

print(f"Health:  {player.health}. Hydration:  {player.hydration}")

# print(f"Player: Health: {player.health} Hunger: {player.hunger} Hydration: {player.hydration} Gold: {player.gold}")

# os.system("cls") # clears the terminal

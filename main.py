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

if player_choise == 3:
  random_hit = 1 # """random.randint(1,2)"""
  if random_hit == 1:
    print(f"You attaced an enemy. He took {player.damege} damage.")
    enemy.health -= player.damege


print(f"Health:  {player.health}. Hydration:  {player.hydration}")
print(f"Enemy: Health: {enemy.health} Gold: {enemy.gold}")

# print(f"Player: Health: {player.health} Hunger: {player.hunger} Hydration: {player.hydration} Gold: {player.gold}")

# os.system("cls") # clears the terminal

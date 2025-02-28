import random
import os

class Player:
  def __init__(self, health, hydration, gold, damag):
    self.health = health
    self.hydration = hydration
    self.gold = gold
    self.dameg = damag
  
class Enemy:
  def __init__(self, health, gold, damag):
    self.health = health
    self.gold = gold
    self.dameg = damag

class Food:
  def __init__(self, food_name, regenerate_food):
    self.food_name = food_name
    self.regenerate_food = regenerate_food

class Drinks:
  def __init__(self, drink_name, regenerate_hydration):
    self.drink_name = drink_name
    self.regenerate_hydration = regenerate_hydration
    
  

player = Player(10, 10, 0, 3)
enemy = Enemy(10, 5, 3)
meet = Food("meet", 5)
water = Drinks("water", 3)

player_choise = int(input("1. Eat: \n2. Drink: \n3. \nwhat do you want to do: "))

if player_choise == 1:
  player.health += meet.regenerate_food

if player.health > 10:
  player.health = 10

if player_choise == 2:
  player.hydration += water.regenerate_hydration

if player.hydration > 10:
  player.hydration == 10

print("Health: ", player.health, "Hydration: ", player.hydration)

# print("Player: ","Health: ", player.health, "Hunger: ", player.hunger, "Hydration: ", player.hydration, "Gold: ", player.gold)

# os.system("cls") # clear the terminal

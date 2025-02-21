import random
import os

class Player:
  def __init__(self, health, hunger, hydration, gold, damag):
    self.health = health
    self.hunger = hunger
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
    
  

player = Player(10, 10, 10, 0, 3)
enemy = Enemy(10, 5, 3)
meet = Food("meet", 3)

player_choise = str(input("1. Eat: \nwhat do you want to do: "))

# print("Player: ","Health: ", player.health, "Hunger: ", player.hunger, "Hydration: ", player.hydration, "Gold: ", player.gold)

# os.system("cls") clear the terminal


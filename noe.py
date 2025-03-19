import random
import os

class Player:
  def __init__(self, health, hydration, gold, damage):
    self._health = health
    self._hydration = hydration
    self.gold = gold
    self.damege = damage

  @property
  def hydration(self):
    if self._hydration >= 10:
      self._hydration = 10
    return self._hydration
  
  @hydration.setter
  def hydration(self, value):
    if value > 10:
      self._hydration = 10
    else:
      self._hydration = value
    
  
  @hydration.deleter
  def hydration(self):
    del self._hydration

  @property
  def health(self):
    if self._health >= 10:
      self._health = 10
    return self._health
  
  @health.setter
  def health(self, value):
    if value > 10:
      self._health = 10
    else:
      self._health = value
  
  @health.deleter
  def health(self):
    del self.hydration

# Change all damag with damage
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

if player_choise == 2:
  player.hydration += water.regenerate_hydration

print(f"Health:  {player.health}. Hydration:  {player.hydration}")

# print(f"Player: Health: {player.health} Hunger: {player.hunger} Hydration: {player.hydration} Gold: {player.gold}")

# os.system("cls") # clear the terminal

import random

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



player = Player(10, 10, 10, 0, 3)
enemy = Enemy(10, 5, 3)

print("Player: ","Health: ", player.health, "Hunger: ", player.hunger, "Hydration: ", player.hydration, "Gold: ", player.gold)  

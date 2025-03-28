import random 
import os
import time
from player import Player
from enemie import Enemie
from food import Food
from drinks import Drinks
from weapons import Weapons


player = Player(10, 10, 0, 3) # Health, Hydration, Gold, Damage
enemie = Enemie(10, 5, 3) # Health, Gold, Damage
meat = Food("meat", 5)
water = Drinks("water", 3)
sword = Weapons("sword", 3)

inventory = []

while True:
  while True:
    try:
      player_choise = int(input("\n1. Eat: \n2. Drink: \n3. Fight: \n4. Show stats: \n5. Seartch for water \n6. Seartch for food \n7. Quit the game \n8. Open inventory \n9. Shop \nWhat do you want to do: "))
    except:
      print("Invalid input")
      time.sleep(3)
      os.system("clear") # clears the terminkllaaa
      continue
    break
  if player_choise == 1:
    if "meat" in inventory:
      player.health += meat.regenerate_food
      print(f"\nPlayer: Health: {player.health}.")
      inventory.remove("meat")
    elif not "meat" in inventory:
      print("You dont have meat in your inventory")
  
  elif player_choise == 2:
    if "water" in inventory:
      player.hydration += water.regenerate_hydration
      print(f"\nPlayer: Hydration. {player.hydration}")
      inventory.remove("water")
    elif not "water" in inventory:
        print("You don't have water in your inventory")  


  elif player_choise == 3:
    random_hit = random.randint(1,2)
    print(random_hit)
    if random_hit == 1:
      print(f"You attaced an enemie. He took {player.damege} damage.")
      enemie.health -= player.damege
      if enemie.health <= 0:
        player.gold += enemie.gold
        print("You killed the enemie!")
        enemie = Enemie(10, 5, 3)
    elif random_hit == 2:
      print(f"The enemie attaked you. You took {enemie.damege} damage.")
      player.health -= enemie.damege
      if player.health <= 0:
        print("You're dead!")
        break
    print(f"\nPlayer: Health:  {player.health}. Hydration:  {player.hydration}")
    print(f"Enemie: Health: {enemie.health} Gold: {enemie.gold}\n")

  elif player_choise == 4:
   print(f"\nPlayer: Health: {player.health}. Hydration: {player.hydration}. Gold: {player.gold}.")
  
  elif player_choise == 5:
    random_seartch_water = random.randint(1,3)
    if random_seartch_water <= 1:
      print("You found some water!")
      inventory.append("water")
    elif random_seartch_water > 1:
      print("You found nothing")

  elif player_choise == 6:
    random_seartch_food = random.randint(1,3)
    if random_seartch_food <= 1:
      print("You found some food!")
      inventory.append("meat")
    elif random_seartch_food > 1:
      print("You found nothing")
  
  elif player_choise == 7:
    print("Good bye my friend!")
    break

  elif player_choise == 8:
    print(f"Inventory: {inventory}")
    if "sword" in inventory:
      player_choise_weapon = input("Dou you want to equip a weapon (Y/N): ").lower()
      if player_choise_weapon == "y":
        player.damege += sword.damage
        inventory.remove("sword")
      elif player_choise_weapon == "n":
        time.sleep(3)
        os.system("clear") # clears the terminkllaaa
        continue
      else:
        print("That is not an option!")
      
  elif player_choise == 9:
    pass
    

  time.sleep(3)
  os.system("clear") # clears the terminkllaaa

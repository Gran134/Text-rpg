import random 
import os
import time
from player import Player
from enemie import Enemie
from food import Food
from drinks import Drinks
from weapons import Weapons
from shop import Shop

os.system("clear")

player = Player(10, 10, 0, 3) # Health, Hydration, Gold, Damage
enemie = Enemie(10, 5, 3) # Health, Gold, Damage
raw_meat = Food("raw meat", 5)
cooked_meat = Food("cooked meat", 7)
dirty_water = Drinks("dirty water", 3)
clean_water = Drinks("clean water", 7)
sword = Weapons("sword", 3)
inventory = player.inventory
food = []
dirty_food = []

while True:
  while True:
    try:
      player_choise = int(input("---Text RPG---\n\n1. Fight: \n2. Show stats: \n3. Seartch for water \n4. Seartch for food \n5. Shop \n6. Open inventory \n7. Quit the game \nWhat do you want to do: "))
    except:
      print("Invalid input")
      time.sleep(3)
      os.system("clear") # clears the terminkllaaa
      continue
    break

  if player_choise == 1:
    os.system("clear")
    random_hit = random.randint(1,2)

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
    player.hydration -= 3
    print(f"\nPlayer: Health:  {player.health}. Hydration: {player.hydration}")
    print(f"Enemie: Health: {enemie.health} Gold: {enemie.gold}\n")

  elif player_choise == 2:
   os.system("clear")
   print(f"---Stats---\nPlayer: Health: {player.health}. Hydration: {player.hydration}. Gold: {player.gold}.")
  
  elif player_choise == 3:
    os.system("clear")
    print("---Searching for water---\n")
    time.sleep(1)
    random_seartch_water = random.randint(1,3)
    player.hydration -= 3

    if random_seartch_water <= 2:
      print("You found some dirty water!")
      inventory.append("dirty water")
      dirty_food.append("dirty water")

    elif random_seartch_water > 2:
      print("You found nothing")

  elif player_choise == 4:
    os.system("clear")
    print("---Searching for food---\n")
    time.sleep(1)
    random_seartch_food = random.randint(1,3)
    player.hydration -= 3

    if random_seartch_food <= 2:
      print("You found some food!")
      inventory.append("raw meat")
      dirty_food.append("raw meat")

    elif random_seartch_food > 2:
      print("You found nothing")
  
  elif player_choise == 5:
    os.system("clear")
    Shop.display_shop()
    player_choise_shop = str(input("What do you want to buy? (exit to exit the shop): ")).lower()
    Shop.buy_item(player, player_choise_shop)
    player.hydration -= 3
  
  elif player_choise == 6:
    os.system("clear")
    player.show_inventory()

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

    elif food or dirty_food:
      while True:
        try:
          player_choise_food = str(input(f"\nWhat food do you want to eat? (N to contineu): ")).lower()
        except:
          print("Invalid input")
          time.sleep(2)
          os.system("clear")
          continue
        break

      if player_choise_food == "cooked meat":
        if "cooked meat" in inventory:
          player.health += cooked_meat.regenerate_food
          player.inventory.remove("cooked meat")
          food.remove(cooked_meat.food_name)
          print(f"Player: Health: {player.health}")
        
        else:
          print(f"You dont have {player_choise_food}")
      
      elif player_choise_food == "clean water":
        if "clean water" in inventory:
          player.inventory.remove("clean water")
          food.remove(clean_water.drink_name)
          player.hydration += clean_water.regenerate_hydration
          print(f"Player: Hydration: {player.hydration}")
        
        else:
          print(f"You dont have {player_choise_food}")

      elif player_choise_food == "n":
        print("Closing inventory")
        time.sleep(2)
        os.system("clear")

        if dirty_food:
          while True:
            try:
              player_choise_cooking = str(input("Do you want to cook your food? (Y/N): ")).lower()
            except:
              print("That is an invalid option")
              continue
            break

          if player_choise_cooking == "y":
            if "raw meat" in dirty_food:
              print("--- Cooking your food ---\n")
              dirty_food.remove("raw meat")
              inventory.remove("raw meat")
              food.append("cooked meat")
              inventory.append("cooked meat")
              time.sleep(1)
              print("You hav cooked food now!")
            
            if "dirty water" in dirty_food:
              print("--- Purifying your water ---\n")
              dirty_food.remove("dirty water")
              inventory.remove("dirty water")
              food.append("clean water")
              inventory.append("clean water")
              time.sleep(1)
              print("You have clean water now")
          
          elif player_choise_cooking == "n":
            print("Exiting inventory")
          else:
            print("Nothing to cook")
      
      else:
        print("That is not an option")
    

  
  
  elif player_choise == 7:
    os.system("clear")
    print("Good bye my friend!")
    break
    

  time.sleep(2)
  os.system("clear") # clears the terminkllaaa

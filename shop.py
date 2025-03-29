import os
shop_items = {
    "sword" : 20,
    "cooked meat" : 10,
    "clean water" : 5
}


class Shop:
    @staticmethod
    def display_shop():
        print("---shop---\n")
        for item, price in shop_items.items():
            print(f"{item}: {price} gold")
        print("------------------")

    @staticmethod   
    def buy_item(player, item_name):
        if item_name in shop_items:
            price = shop_items[item_name]
            if player.gold >= price:
                player.gold -= price
                player.inventory.append(item_name)
                print(f"You bought {item_name} for {price} gold. You now have {player.gold} gold left.")
            else:
                print("Not enough gold!")
        elif item_name == "exit":
                    os.system("clear")
                    print("---Exiting the shop---")
        else:
            print("Item not found!")
class Player:
  def __init__(self, health, hydration, gold, damage):
    self._health = health
    self._hydration = hydration
    self.gold = gold
    self.damege = damage
    self.inventory = []

  def show_inventory(self):
        if self.inventory:
            print("--- Inventory ---\n")
            for item in self.inventory:
                print(f"- {item}")
            print("-----------------")
        else:
            print("--- Inventory ---\nYour inventory is empty!\n-----------------")

  @property
  def hydration(self):
    if self._hydration > 10:
      self._hydration = 10
    return self._hydration
  
  @hydration.setter
  def hydration(self, value):
    if value > 10:
      self._hydration = 10
    elif value <= 0:
      self._hydration = 0
    else:
      self._hydration = value
    
  
  @hydration.deleter
  def hydration(self):
    del self._hydration

  @property
  def health(self):
    if self._health > 10:
      self._health = 10
    return self._health
  
  @health.setter
  def health(self, value):
    if value > 10:
      self._health = 10
    elif value <= 0:
      self._health = 0
    else:
      self._health = value
  
  @health.deleter
  def health(self):
    del self.hydration

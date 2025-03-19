class Enemy:
  def __init__(self, health, gold, damage):
    self.health = health
    self.gold = gold
    self.damege = damage
  
  @property
  def health(self):
    if self._health > 9:
      self._health = 9
    return self._health
  
  @health.setter
  def health(self, value):
    if value > 9:
      self._health = 9
    elif value <= -1:
      self._health = -1
    else:
      self._health = value
  
  @health.deleter
  def health(self):
    del self.hydration
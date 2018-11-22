class Player:
  def __init__(self, width, height, speed, posx, posy):
    self.width = width
    self.height = height
    self.speed = speed
    self.posx = posx 
    self.posy = posy

  def move_x(self, dir):
    self.posx += dir * self.speed

  def move_y(self, dir):
    self.posy += dir * self.speed
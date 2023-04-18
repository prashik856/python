class Rectangle:
 def __init__(self,length,width):
  self.length=length
  self.width=width

 def cal_area(self):
  return self.length*self.width

 @classmethod
 def new_sq(cls,side_length):
  return cls(side_length,side_length)

square=Rectangle.new_sq(6)
print(square.cal_area())

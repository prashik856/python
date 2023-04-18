class Pizza:
 def __init__(self,toppings):
  self.toppings=toppings
 
 def pi(self):
  print(self.toppings)

 @staticmethod
 def validate_topping(topping):
  if topping=='pineapple':
   raise ValueError('No pineapples')
  else:
   return True

ingredients=['cheese','onions','spam']
if all(Pizza.validate_topping(i) for i in ingredients):
 pizza=Pizza(ingredients)
 pizza.pi()

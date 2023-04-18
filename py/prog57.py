def decor(func):
 def wrap():
  print('==========')
  func()
  print('==========')
 return wrap

def print_text():
 print('hello world')
 print('chutiya')

decorated=decor(print_text)
decorated()

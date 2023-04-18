while True:
 print('Options')
 print('Enter \'add\' to add two numbers')
 print('Enter \'subtract\' to subtract two numbers')
 print('Enter \'multiply\' to multiply two numbers')
 print('Enter \'divide\' to divide two numbers')
 print('Enter \'quit\' to exit')
 user_input=input(':')
 if user_input=='quit':
  break
 elif user_input=='add':
  try:
   num1=float(input('Enter a number:'))
   num2=float(input('Enet another number:'))
  except:
   print('invalid input')
  result=str(num1+num2)
  print('The answer is ' + result)   
 elif user_input=='subtract':
  num1=float(input('Enter a number:'))
  num2=float(input('Enet another number:'))
  result=str(num1-num2)
  print('The answer is ' + result)
 elif user_input=='multiply':
  num1=float(input('Enter a number:'))
  num2=float(input('Enet another number:'))
  result=str(num1*num2)
  print('The answer is ' + result)
 elif user_input=='divide':
  num1=float(input('Enter a number:'))
  num2=float(input('Enet another number:'))
  result=str(num1/num2)
  print('The answer is ' + result)
 else :
  print('Unknown Input')

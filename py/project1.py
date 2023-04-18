def count(f,char):
 a=0
 for i in f:
  if i==char:
   a=a+1
 return a

flag=0
flag1=0

while flag==0:
  filename=input('Input a file name or input quit to exit:')
  if filename=='quit':
   flag1=1
   break
  else:
   try:
    f=open(filename,'r')
    flag=1
   except:
    print('Invalid file name. Please enter a valid file name, if you want to quit, enter quit.')

if flag1==1:
 print('Thank you for using our program')

if flag==1:
 r=f.read()
 print('The file you asked for is: ',filename)
 print(r)
 b=len(r)
 for char in 'abcdefghijklmnopqrstuvwxyz':
  a=count(r,char)
  print('{}-{}%'.format(char,(a/b)*100))
 

class ss:
 def __init__(self,cont):
  self.cont=cont

 def __truediv__(self,other):
  line='='*len(other.cont)
  return '\n'.join([self.cont,line,other.cont])

spam=ss('spam')
hello=ss('helloworld')
print(spam/hello)

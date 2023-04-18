import random

class VL:
 def __init__(self,cont):
  self.cont=cont

 def __getitem__(self,index):
  return self.cont[index + random.randint(-1,1)]
 
 def __len__(self):
  return random.randint(0,len(self.cont)*2)

vl=VL(['a','b','c','d','e'])
print(len(vl))
print(len(vl))
print(vl[2])
print(vl[2])

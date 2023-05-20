'''
class PartyAnimal:
   x = 0
   name = ''
   def __init__(self, nam):
     self.name = nam
     print(self.name,'constructed')

   def __del__(self):
     print('I am destructed', self.x)

   def party(self) :
     self.x = self.x + 1
     print(self.name,'party count',self.x)
     print("So far",self.x)

an = PartyAnimal()
print ("Type", type(an))
print ("Dir ", dir(an))
print ("Type", type(an.x))
print ("Type", type(an.party))

an.party()
an.party()
an = 42
print('an contains',an)

s = PartyAnimal('Sally')
j = PartyAnimal('Jim')

s.party()
j.party()
s.party()
j.six()
print(dir(j))

***********************************************************************



'''
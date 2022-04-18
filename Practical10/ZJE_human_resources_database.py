import re
class Staff(object):
  def __init__(self,name,location,role):
     self.name=name
     self.location=location
     self.role=role
  def data (self):
     number=len(re.split(r'[,;]+',self.name))
     name_split=re.split(r'[,;]+',self.name)
     location_split=re.split(r'[,;]+',self.location)
     role_split=re.split(r'[,;]+',self.role)
     for i in range (0,number):
         print (name_split[i],";",location_split[i],";",role_split[i])

a=input("The first and last name of the staff (separate with ; or ,):")
b=input("The location of the staff (separate with ; or ,):")
c=input("The role of the staff (separate with ; or ,):")
k=Staff(a,b,c)
k.data()

#Example
x="Xu Ziling,Li Jiajia,Cui Meng,Zhang Hao,Mei Li"
y="International campus,international campus,international campus,Edinburgh,Endinburgh,international campus"
z="faculty,faculty,leadership,administration,faculty"
c=Staff(x,y,z)
c.data()

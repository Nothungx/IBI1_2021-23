import numpy as np
import matplotlib.pyplot as plt

a='30' #a,b,c,d,e,f,g,h,i,j represent the variables for the age.
b='35'
c='40'
d='45'
e='50'
f='55'
g='60'
h='65'
i='70'
j='75'
CHD={a:1.03,b:1.07,c:1.11,d:1.17,e:1.23,f:1.32,g:1.42,h:1.55,i:1.72,j:1.94}
print (CHD)

N=10 #There are 10 paternal ages corresponding to 10 CHD
x=[30,35,40,45,50,55,60,65,70,75] #x's values show the paternal ages
y=[1.03,1.07,1.11,1.17,1.23,1.32,1.42,1.55,1.72,1.94] #y's values shows the risk of CHD for the offspring corresponding to paternal ages
plt.ylabel('CHD') #Set the y label
plt.xlabel('paternal age') # Set the x label
plt.scatter(x,y,marker='o')
plt.show()

age=input("The paternal age is:") #Age repesents the requested paternal age.
print ("The CHD of",age,"is",CHD[age]) #Show the requested paternal age's corresponding CHD for the offspring.

import numpy as np
import matplotlib.pyplot as plt

CHD={'30':1.03,'35':1.07,'40':1.11,'45':1.17,'50':1.23,'55':1.32,'60':1.42,'65':1.55,'70':1.72,'75':1.94}
print (CHD)

N=10 #There are 10 paternal ages corresponding to 10 CHD
x=[30,35,40,45,50,55,60,65,70,75] #x's values show the paternal ages
y=[1.03,1.07,1.11,1.17,1.23,1.32,1.42,1.55,1.72,1.94] #y's values shows the risk of CHD for the offspring corresponding to paternal ages
plt.ylabel('CHD') #Set the y label
plt.xlabel('paternal age') # Set the x label
plt.scatter(x,y,marker='o')
plt.show()

age='55' #Age repesents the requested paternal age.
print (CHD['55']) #Show the requested paternal age's corresponding CHD for the offspring.

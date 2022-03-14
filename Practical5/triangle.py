#set variable n as triangle sequence and x as xth triangle number
n=1
x=1
#compute and display the first 10 triangle sequence
for i in range(0,10):
   n=x*(x+1)/2
   print (n)
   x=x+1

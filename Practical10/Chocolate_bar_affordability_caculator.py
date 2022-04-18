def Chocolate(x,y):
    number=int(x/y)
    change=x-number*y
    print ("Can bought",number,"bars of chocolate and left over",change,"change.")
    return number,change

a=input("Total money:")
b=input("Price of one bar of chocolate:")
print(Chocolate(a,b))

#Example
x=100
y=7
print(Chocolate(x,y))


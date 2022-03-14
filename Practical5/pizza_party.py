#Set the n variables as number of cuts and p as the number of pieces.
n=1
p=2
print (n,"straight cut can make",p,"slices")
#Calculate the p for an increasing number of n until p=64. Print the output sentence.
while p<64:
   n=n+1
   p=(n*n+n+2)/2
   print (n,"straight cuts can make",p,"slices.")

print (n,"straight cuts can make",p,"slices, which can meet the need for each member of the IBI1 class.")

import numpy as np
import matplotlib.pyplot as plt

#Clear the list.
a_list=[]
#Set the 'marks' as Rob's marks.
marks=[45,36,86,57,53,92,65,45] #Rob's marks.
L=marks
L.sort() #Sort Rob's marks.
print (L)

avg=sum(marks)/len(marks)
if avg<60:
   print("Rob's average mark is",avg,"so he failed this ICA.")
else:
   print("Rob's average mark is",avg,"so he passed this ICA.")

#Make boxplot of Rob's marks.
n=8
plt.boxplot(marks,
            vert=True,
            whis=1.5,
            patch_artist=True,
            meanline=True,
            showbox=True,
            showcaps=True,
            showfliers=True,
            notch=False)
plt.title("Boxplot of Rob's marks")
plt.ylabel("Marks")
plt.xlabel("Rob")
plt.show()


import numpy as np
import matplotlib.pyplot as plt

#Clear the list.
a_list=[]
#Set the 'marks' as Rob's marks.
marks=[45,36,86,57,53,92,65,45] #Rob's marks.
L=marks
L.sort() #Sort Rob's marks.
print (L)

#Make boxplot of Rob's marks.
n=8
plt.boxplot(marks,
            vert=True,
            whis=1.5,
            patch_artist=True,
            meanline=False,
            showbox=True,
            showcaps=True,
            showfliers=True,
            notch=False)
plt.show()

#Rob's average mark is 59.875, so he failed this ICA.


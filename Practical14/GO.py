from xml.dom.minidom import parse
import xml.dom.minidom
import numpy as np
import matplotlib.pyplot as plt
import re

DOMTree=xml.dom.minidom.parse("xid-781202_1.xml")
collection=DOMTree.documentElement
terms=collection.getElementsByTagName("term")
count_child=0
count_term=0
child_L=[]
child_L1=[]

for term in terms:
    count_term=count_term+1
    child=term.getElementsByTagName("is_a")
    count_child=len(child)
    child_L.append(count_child)
print("The total number of terms are",count_term)

plt.boxplot(child_L,meanline=True)
plt.xlabel("terms")
plt.ylabel("childnodes numbers")
plt.title("The distribution of the number of childnodes associated with each term")
plt.show()

for term in terms:
    defstr=term.getElementsByTagName("defstr")[0]
    defstr1=str(defstr.childNodes[0].data)
    if re.findall("translation",defstr1):
       child1=term.getElementsByTagName("is_a")
       count_child1=len(child1)
       child_L1.append(count_child1)

plt.boxplot(child_L1)
plt.xlabel("terms associated with translation")
plt.ylabel("childnodes numbers")
plt.title("The distribution of the number of childnodes associated with terms with translation")
plt.show()

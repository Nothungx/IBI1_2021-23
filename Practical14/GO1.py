from xml.dom.minidom import parse
import xml.dom.minidom
import numpy as np
import matplotlib.pyplot as plt
import re
from collections import defaultdict

DOMTree=xml.dom.minidom.parse("xid-781202_1.xml")
collection=DOMTree.documentElement
terms=collection.getElementsByTagName("term")
dic=defaultdict(list)
dic1=defaultdict(list)
count_term=0
child_L=[]
child_L1=[]

for term in terms:
    count_term=count_term+1
    parent1=term.getElementsByTagName("is_a")
    parent_number=len(parent1)
    child=term.getElementsByTagName("id")[0]
    childid=child.childNodes[0].data
    for i in range (0,parent_number):
        parent=term.getElementsByTagName("is_a")[i]
        parentid=parent.childNodes[0].data
        dic[parentid].append(childid)
print ("The total number of terms are",count_term)

for term in terms:
    parent=term.getElementsByTagName("id")[0]
    parentid=parent.childNodes[0].data
    if parentid in dic:
       child_L.append(len(dic[parentid]))

plt.boxplot(child_L)
plt.xlabel("terms")
plt.ylabel("childnodes numbers")
plt.title("The distribution of the number of childnodes associated with each term")
plt.show()


for term in terms:
    defstr=term.getElementsByTagName("defstr")[0]
    defstr1=str(defstr.childNodes[0].data)
    if re.findall("translation",defstr1):
       parent1=term.getElementsByTagName("is_a")
       parent_number=len(parent1)
       child=term.getElementsByTagName("id")[0]
       childid=child.childNodes[0].data
       for i in range (0,parent_number):
           parent=term.getElementsByTagName("is_a")[i]
           parentid=parent.childNodes[0].data
           dic1[parentid].append(childid)

for term in terms:
    parent=term.getElementsByTagName("id")[0]
    parentid=parent.childNodes[0].data
    if parentid in dic1:
       child_L1.append(len(dic1[parentid]))

plt.boxplot(child_L1)
plt.xlabel("terms with translation")
plt.ylabel("childnodes numbers")
plt.title("The distribution of the number of childnodes associated with terms with translation")
plt.show()

def average(list):
    sum=0
    for item in list:
        sum+=item
    return sum/len(list)
print (average(child_L),average(child_L1))
#The "translation" termscontain a smaller number of child nodes than the overall Gene Ontology. The number of child nodes of "translation" terms is 1.938 while the overall is 4.396.
print ("The 'translation' terms contain a smaller number of child nodes than the overall Gene Ontology.")

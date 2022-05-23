from xml.dom.minidom import parse
import xml.dom.minidom
import numpy as np
import matplotlib.pyplot as plt
import re
from collections import defaultdict
from functools import lru_cache
import json
import pandas as pd

DOMTree = xml.dom.minidom.parse("xid-781202_1.xml")
collection = DOMTree.documentElement
terms = collection.getElementsByTagName("term")


# Dictionary for parent nodes, the value is list of children
dic_parent = defaultdict(list)
dic_defstr = dict()

all_terms = set()
count_term=0

for term in terms:
    count_term=count_term+1
    term_id = term.getElementsByTagName("id")[0].firstChild.data
    all_terms.add(term_id)
    parent_ids = [p.firstChild.data for p in term.getElementsByTagName("is_a")]
    if parent_ids:
        for parent_id in parent_ids:
            dic_parent[parent_id] = dic_parent[parent_id] + [term_id]

    defstr = term.getElementsByTagName('def')[0].getElementsByTagName('defstr')[0]
    dic_defstr[term_id] = set(defstr.firstChild.data.lower().split())

print ("The total number of terms are",count_term)

# Take the child nodes of the child nodes and merge them together. Set is used to delete repetition.
@lru_cache
def get_children(term):
    children = set(dic_parent[term])
    for c in dic_parent[term]:
        children = children.union(get_children(c))

    return children


dict_children = dict()

for t in all_terms:
    dict_children[t] = get_children(t)

dict_children_num = {t: len(dict_children[t]) for t in all_terms}

plt.boxplot(list(dict_children_num.values()))
plt.xlabel("terms")
plt.ylabel("childnodes numbers")
plt.title("The distribution of the number of childnodes associated with every term")
plt.show()


dict_translation = {k: v for k, v in dict_children_num.items() if 'translation' in dic_defstr[k]}

plt.boxplot(list(dict_translation.values()))
plt.xlabel("terms with translation")
plt.ylabel("childnodes numbers")
plt.title("The distribution of the number of childnodes associated with terms with translation")
plt.show()

#The "translation" terms contain a smaller number of child nodes than the overall Gene Ontology.
print ("The 'translation' terms contain a smaller number of child nodes than the overall Gene Ontology.")



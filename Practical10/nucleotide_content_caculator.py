import re

def caculator(L):
    A=len(re.findall(r'[Aa]',L))
    G=len(re.findall(r'[Gg]',L))
    C=len(re.findall(r'[Cc]',L))
    T=len(re.findall(r'[Tt]',L))
    print ("The percentage of nucleotides A is",A/len(L),",G is",G/len(L),",C is",C/len(L),",T is",T/len(L))
    return A,G,C,T

x=input("The DNA strand is ")
caculator(x)

#Example
L="AaGGgCCccTTttT"
caculator(L)

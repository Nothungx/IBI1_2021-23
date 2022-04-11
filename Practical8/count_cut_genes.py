import re
file_name=input("new file name is ")
file_name_fa=file_name+'.fa'
file = open('cut_genes.fa')
fount=open(file_name_fa,'w')
all_gene="s"

for line in file:
    line=line.rstrip()
    all_gene=all_gene+line
genes=re.split(r'>',all_gene)


for i in range(1,len(genes)):
    x=genes[i]
    fragments= re.findall(r'GAATTC',x)
    name=x[:7]
    number=len(fragments)
    DNA=re.findall(r'\'([A-Z]+)',x)
    line1='>'+name+'   '
    line2=str(number)+'\n'
    line3=str(DNA)+'\n'
    fount.write(line1)
    fount.write(line2)
    fount.write(line3)
fount.close()

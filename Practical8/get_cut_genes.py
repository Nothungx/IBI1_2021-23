import re
file = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
all_gene="s"
fount=open('cut_genes.fa','w')

for line in file:
    line=line.rstrip()
    all_gene=all_gene+line
genes=re.split(r'>',all_gene)

for i in range(0,len(genes)):
    x=genes[i]
    if x.find('GAATTC')>=0:
       name=x[:7]
       length=re.findall(r']([A-Z]+)',x)
       p=len(str(length))-4
       line1='>'+name+'   '
       line2=str(p)+'\n'
       line3=str(length)+'\n'
       fount.write(line1)
       fount.write(line2)
       fount.write(line3)
fount.close()

import re
seq="ATGCAATCGACTACGATCAATCGAGGGCC"
print (seq)
fragments= re.findall(r'GAATTC',seq)
print (len(fragments), "fragment would be cut if EcoRI enzyme was applied to this sequence.")

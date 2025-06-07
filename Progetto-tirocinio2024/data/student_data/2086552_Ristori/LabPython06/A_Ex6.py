numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre=9510990939794952322311710154344301747012051743844839
dita=0
for base in range(100):
    potenza=len(numeraleAlieno)-1
    valore=0
    for x in numeraleAlieno:
        valore=valore+int(x)*base**potenza
        potenza-=1
    if valore==numeroTerrestre:
        dita=base
        break
print(dita)

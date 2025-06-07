numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre=9510990939794952322311710154344301747012051743844839
base=2
valore=0
while valore!=numeroTerrestre:
    base+=1
    valore=0
    potenza=len(numeraleAlieno)-1
    for i in numeraleAlieno:
        valore=valore+int(i)*base**potenza
        potenza=potenza-1
print(base)

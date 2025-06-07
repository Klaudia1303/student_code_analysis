
numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre=9510990939794952322311710154344301747012051743844839


s=numeraleAlieno
valore=0
potenza=len(s)-1

for base in range(1000):
    for c in s:
        valore=valore+int(c)*base**potenza

        potenza=potenza-1
        

    if valore==numeroTerrestre:
        break

    valore=0
    potenza=len(s)-1

    
print(base)

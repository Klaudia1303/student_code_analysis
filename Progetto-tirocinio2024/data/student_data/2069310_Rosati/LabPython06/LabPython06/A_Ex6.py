numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre=9510990939794952322311710154344301747012051743844839

for base in range(2,99999):
    numAlieno = 0
    j = 0
    for i in numeraleAlieno[::-1]:
        numAlieno += int(i)*(base**j)
        j += 1
    print(base,numAlieno)
    if numAlieno == numeroTerrestre:
       print(base)
       break
    

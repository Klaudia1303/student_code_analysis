numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre=9510990939794952322311710154344301747012051743844839

numAl=str(numeraleAlieno)

b=0
boo=True
while boo:
    cif=0
    for i in range(len(numAl)):
        cif=cif+int(numAl[::-1][i])*b**i
    if cif==numeroTerrestre:
        print('Gli alieni hanno',b,'dita')
        break
    b=b+1


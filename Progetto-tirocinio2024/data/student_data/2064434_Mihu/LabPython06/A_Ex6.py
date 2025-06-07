numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre=9510990939794952322311710154344301747012051743844839
corretto=False
k=1
while not corretto:
    valore=0
    potenza=len(numeraleAlieno)-1
    for i in numeraleAlieno:
        valore=valore+int(i)*k**potenza
        potenza=potenza-1
    if valore==numeroTerrestre:
        print(k)
        corretto=True
    else:
        k=k+1

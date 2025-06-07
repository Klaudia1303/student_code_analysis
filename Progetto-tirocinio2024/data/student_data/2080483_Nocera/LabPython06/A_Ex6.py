numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre=9510990939794952322311710154344301747012051743844839
i=2
right=True
while right:
    somma=0
    potenza=len(numeraleAlieno)-1
    for c in numeraleAlieno:
        somma+=int(c)*i**potenza
        potenza-=1
    if somma==numeroTerrestre:
        print(i)
        right=False
    else:
        i+=1
            

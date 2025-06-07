numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre=9510990939794952322311710154344301747012051743844839
somma=0
precedente=0
for i in range(1,len(numeraleAlieno)):
    for j in range(len(numeraleAlieno)):
        x=int(numeraleAlieno[j])
        y=len(numeraleAlieno)-1-j
        z=x*(i**y)
        somma=z+precedente
        precedente=somma
    if somma==numeroTerrestre:
        print(i)
        break
    else:
        precedente=0
        y=0

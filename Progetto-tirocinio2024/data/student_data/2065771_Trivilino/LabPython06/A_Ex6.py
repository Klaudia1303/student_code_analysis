numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre=9510990939794952322311710154344301747012051743844839

risultato= 0
baseattuale= 1

while True:
    accumulatore= 0
    potenza = len(numeraleAlieno) - 1
    for i in numeraleAlieno:
        accumulatore+=int(i)*baseattuale**potenza
        potenza-=1

    if accumulatore==numeroTerrestre:
        break
    baseattuale+=1

print(baseattuale)

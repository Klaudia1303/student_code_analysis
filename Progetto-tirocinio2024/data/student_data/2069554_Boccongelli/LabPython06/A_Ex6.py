numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre=9510990939794952322311710154344301747012051743844839

n = 0
while True:
    somma = 0
    for i in range(len(str(numeraleAlieno))):
        somma += int(str(numeraleAlieno)[::-1][i])*n**i
    if (somma == numeroTerrestre):
        print('Gli alieni usano la base: ', n)
        break
    n += 1

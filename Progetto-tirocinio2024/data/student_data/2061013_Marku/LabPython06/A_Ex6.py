numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre=9510990939794952322311710154344301747012051743844839
somma=0
base=11
while base>=11:
    somma=0
    potenza=len(numeraleAlieno)-1
    for i in range(len(numeraleAlieno)):
        numero=int(numeraleAlieno[i])*base**potenza
        somma+=numero
        potenza-=1
    if somma==numeroTerrestre:
        print(base)
        break
    base+=1


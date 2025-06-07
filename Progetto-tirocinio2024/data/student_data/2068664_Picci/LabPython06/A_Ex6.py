numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre=9510990939794952322311710154344301747012051743844839

esp=41
somma=0
p=numeroTerrestre
for i in range(2,p):
    for j in range(0,len(numeraleAlieno)):
        somma=somma+int(numeraleAlieno[j])*(i**esp)
        esp=esp-1
    if somma==numeroTerrestre:
        print(i)
    else:
        somma=0
        esp=41


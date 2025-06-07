numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre=9510990939794952322311710154344301747012051743844839
for i in range(11,len(numeraleAlieno)):
    numA=0
    for j in range(len(numeraleAlieno)):
        numA+=int(numeraleAlieno[len(numeraleAlieno)-j-1])*(i**j)
    if numA==numeroTerrestre:
        break
print('numero dita degli alieni: ',i)

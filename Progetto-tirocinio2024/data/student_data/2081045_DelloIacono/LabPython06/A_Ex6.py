numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre=9510990939794952322311710154344301747012051743844839
for i in range(11, len(numeraleAlieno)):
    num = 0
    for j in range(len(numeraleAlieno)):
        num = num + int(numeraleAlieno[len(numeraleAlieno)-1-j])*pow(i,j)
    if (num == numeroTerrestre):
        break
print(i)

numeroAlieno='349776123345679876543234567876543234569055'
numeroTerrestre=9510990939794952322311710154344301747012051743844839
for i in range (11,len(numeroAlieno)):
    n = 0
    for j in range (len(numeroAlieno)):
        n += int(numeroAlieno[len(numeroAlieno)-1-j])*pow(i,j)
    if n == numeroTerrestre:
        break
print(i)

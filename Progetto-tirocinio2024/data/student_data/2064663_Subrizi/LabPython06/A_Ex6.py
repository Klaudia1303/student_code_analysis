numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre=9510990939794952322311710154344301747012051743844839
x=int(numeraleAlieno)
for j in range(1, x+1):
    numA=0
    for i in range(0, len(numeraleAlieno)):
        numA+=int(numeraleAlieno[i])*(j**(len(numeraleAlieno)-1-i))
    if numeroTerrestre==numA:
        print(j)
        break






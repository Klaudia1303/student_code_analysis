numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre=9510990939794952322311710154344301747012051743844839
numero=0
x=0
potenza=0
while numeroTerrestre!=numero:
    numero=0
    potenza=0
    x+=1
    for pos in range(len(numeraleAlieno)-1,-1,-1):   
        numero=numero+(x**potenza)*int(numeraleAlieno[pos])
        potenza+=1
print(x)
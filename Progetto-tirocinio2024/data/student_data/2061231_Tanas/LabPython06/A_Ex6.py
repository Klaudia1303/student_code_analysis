numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre=9510990939794952322311710154344301747012051743844839

for base in range(100):
    temp = 0
    for i in range(len(numeraleAlieno)):
        temp += int(numeraleAlieno[i])*(base**(len(numeraleAlieno)-1-i))
    
    if temp == numeroTerrestre:
        break

print(base)

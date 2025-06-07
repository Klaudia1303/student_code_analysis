numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre=9510990939794952322311710154344301747012051743844839

primov=0
secondov=0
for i in range(1,1001):
    primov=20*i
    secondov=secondov+i
    if primov==secondov:
        break
print(i)
    

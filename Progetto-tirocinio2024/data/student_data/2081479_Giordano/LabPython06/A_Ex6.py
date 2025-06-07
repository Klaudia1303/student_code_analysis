numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre=9510990939794952322311710154344301747012051743844839

newBase=7
transformNumber=''
newBaseNumber=numeroTerrestre
while transformNumber!=numeraleAlieno:    
    while newBaseNumber//newBase!=0:
        transformNumber=str(newBaseNumber%newBase)+transformNumber
        newBaseNumber=newBaseNumber//newBase
    if newBaseNumber//newBase==0:
        transformNumber=str(newBaseNumber)+transformNumber
    if transformNumber!=numeraleAlieno:
        transformNumber=''
        newBase+=1
        newBaseNumber=numeroTerrestre
print('dita alieni:',newBase)



numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre=9510990939794952322311710154344301747012051743844839

numero=0
base=2
while not numero==numeroTerrestre:
    numero=0
    posiz=len(numeraleAlieno)-1
    for i in numeraleAlieno:
        numero=numero+int(i)*(base**posiz)
        posiz-=1
    base+=1
print(base)
    
    
    










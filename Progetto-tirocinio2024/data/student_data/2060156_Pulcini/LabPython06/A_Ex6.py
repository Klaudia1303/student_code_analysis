numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre=9510990939794952322311710154344301747012051743844839

for baseAliena in range(2,100000):
    x=0
    j=0
    for i in numeraleAlieno[::-1]:
        x+=int(i)*(baseAliena**j)
        j+=1
        
    if x==numeroTerrestre:
        print(baseAliena)
        break

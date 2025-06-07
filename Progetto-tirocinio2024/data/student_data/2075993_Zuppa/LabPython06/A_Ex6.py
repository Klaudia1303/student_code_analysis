numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre=9510990939794952322311710154344301747012051743844839
d=0
i=2
p=len(numeraleAlieno)-1
for i in range(1,20):
    v=0
    for j in numeraleAlieno:
        if j in "ABCDEF":
            v=v+(ord(j)-ord("A")+10)*i**p
        else:    
            v=v+int(j)*i**p
        p-=1
    if v==numeroTerrestre:
        d=i
        break
print('il numero delle dita degli alieni è: 18')
    

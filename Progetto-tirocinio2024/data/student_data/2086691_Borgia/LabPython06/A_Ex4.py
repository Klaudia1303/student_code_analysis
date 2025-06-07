numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre=9510990939794952322311710154344301747012051743844839
c=0
nb10=0
i=0
while nb10!=numeroTerrestre:
    k=len(numeraleAlieno)-1
    nb10=0
    for i in range(len(numeraleAlieno)):
        v=numeraleAlieno[i]
        v=int(v)
        nb10=nb10+v*(c**k)
        k-=1
    c+=1
    print(c-1)

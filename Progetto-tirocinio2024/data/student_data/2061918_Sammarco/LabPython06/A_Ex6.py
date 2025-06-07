numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre=9510990939794952322311710154344301747012051743844839
for i in range(1,10000):
    NumA=0
    r=0
    for j in numeraleAlieno[::-1]:
        NumA+=int(j)*(i**r)
        r+=1
        if NumA==numeroTerrestre:
            print(i)
            break

numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre=9510990939794952322311710154344301747012051743844839


na2= numeraleAlieno[::-1]
for i in range(11,1011):
    nr=0
    for j in range(len(numeraleAlieno)):
        nr += int(na2[j])*i**j
        if nr==numeroTerrestre:
            print(i)
            break
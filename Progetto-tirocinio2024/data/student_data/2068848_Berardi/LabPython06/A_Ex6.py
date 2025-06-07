numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre=9510990939794952322311710154344301747012051743844839
na = numeraleAlieno
nt = numeroTerrestre
for i in range(2,nt):
    e = len(na)-1
    temp_nt = 0
    for j in range(0,len(na)):
        temp_nt += int(na[j])*(i**e)
        e -= 1
    if temp_nt == nt:
        print("BASE:",i)
        break
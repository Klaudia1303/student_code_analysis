numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre=9510990939794952322311710154344301747012051743844839
m=0
k=41
for n in range(10,20):
    for i in numeraleAlieno:
        if m==numeroTerrestre:
            break
        else:
            m=m+int(i)*(n**k)
            k=k-1
    if m==numeroTerrestre:
        break
    m=0
    k=41
print("gli alieni hanno",n,"dita")    

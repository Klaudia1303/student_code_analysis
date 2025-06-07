numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre=9510990939794952322311710154344301747012051743844839
s=0
p=11
l=0
while s!=numeroTerrestre:
    s=0
    p=p+1
    for j in range(len(numeraleAlieno)-1,-1,-1):
        s=s+int(numeraleAlieno[j])*p**l
        l=l+1
    print(s)
    l=0

print(p)
        
        
    

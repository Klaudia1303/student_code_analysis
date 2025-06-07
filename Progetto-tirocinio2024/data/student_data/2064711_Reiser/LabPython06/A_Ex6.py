numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre=9510990939794952322311710154344301747012051743844839

k=12
i=0
num=0

while num<numeroTerrestre:
    num0=num
    for i in range(len(numeraleAlieno)):
        num=num+int(numeraleAlieno[i])*k**(len(numeraleAlieno)-1-i)
    k+=1
    i=1
print(k-1)
num=0



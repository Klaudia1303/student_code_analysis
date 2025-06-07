numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre=9510990939794952322311710154344301747012051743844839
NumAl=numeraleAlieno[::-1]
a2=0
n=11
while a2!=numeroTerrestre:
    e=0
    n+=1
    a2=0
    for i in range(len(numeraleAlieno)):
        k=int(NumAl[i])*n**e
        a2+=k
        e+=1
print("gli alieni hanno",n,"dita")

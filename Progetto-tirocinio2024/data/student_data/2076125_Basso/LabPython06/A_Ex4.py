numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre=9510990939794952322311710154344301747012051743844839

d1=0
d2=0

for i in range(1,1000):
    p1=20
    p2=i

    d1=d1+p1
    d2=d2+p2
    print(d1,d2)
    if d2 >= d1:
        break
print(i)

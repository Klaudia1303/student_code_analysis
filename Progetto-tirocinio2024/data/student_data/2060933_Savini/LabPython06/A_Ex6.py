numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre=9510990939794952322311710154344301747012051743844839
x= 0
base= 1
while True:
    i=0
    l = len (numeraleAlieno) -1
    for k in numeraleAlieno:
        i+=int(k)*base**l
        l-= 1
    if i== numeroTerrestre:
        break
    base += 1
print(base)

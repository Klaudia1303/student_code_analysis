numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre=9510990939794952322311710154344301747012051743844839

x=0
d=1
while True:
    acc=0
    y=len(numeraleAlieno) - 1
    for c in numeraleAlieno:
        acc+=int(c)*d**y
        y-= 1
    if acc==numeroTerrestre:
        break
    d+= 1
print(d)

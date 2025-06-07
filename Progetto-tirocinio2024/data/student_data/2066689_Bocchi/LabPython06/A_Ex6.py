numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre=9510990939794952322311710154344301747012051743844839

i=11
somma=0
while somma!=numeroTerrestre:
    somma=0
    x=0
    for c in numeraleAlieno:
        somma= somma +int(c)*i**(len(numeraleAlieno)-1-x)
        x=x+1
    i=i+1
print(i-1)

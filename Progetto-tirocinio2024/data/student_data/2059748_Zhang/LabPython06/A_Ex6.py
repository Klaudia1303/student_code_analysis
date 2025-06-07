numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre=9510990939794952322311710154344301747012051743844839

base=1
out=0

while out!=numeroTerrestre:
    base+=1
    out=sum([int(numeraleAlieno[n])*pow(base,(len(numeraleAlieno)-1-n))
    for n in range (len(numeraleAlieno))])

print("Gli alieni hanno",base,"dita.")

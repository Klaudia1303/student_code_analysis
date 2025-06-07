numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre=9510990939794952322311710154344301747012051743844839
for i in range(11,1000):
    p=len(numeraleAlieno)-1
    TraduzioneNumeraleAlieno=0
    for j in range(0,p+1):
        TraduzioneNumeraleAlieno+=int(numeraleAlieno[j])*i**(p-j)
    if TraduzioneNumeraleAlieno==numeroTerrestre:
        print(i)
        break

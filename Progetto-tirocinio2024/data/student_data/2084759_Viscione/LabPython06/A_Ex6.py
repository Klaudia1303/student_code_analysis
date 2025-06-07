numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre=9510990939794952322311710154344301747012051743844839
uguali=False
x=9
while not uguali:
    Conversione=0
    for i in range(len(numeraleAlieno)):
        Conversione=Conversione+int(numeraleAlieno[i])*(x**(len(numeraleAlieno)-1-i))
    if Conversione==numeroTerrestre:
        uguali=True
        print(x)
    else:
        x=x+1

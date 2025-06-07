import sys
numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre=9510990939794952322311710154344301747012051743844839
risultato=0
base=0
for i in range(1, 1000):
    for y in range (len(numeraleAlieno)-1,-1,-1):
        risultato+=int(numeraleAlieno [y])*(i**(len(numeraleAlieno)-y-1))
    
    if risultato==numeroTerrestre:
            print(i)
            sys.exit(0)
    else:
        risultato=0

    

numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre=9510990939794952322311710154344301747012051743844839
base = 2
potenza = len(numeraleAlieno) -1
numero = 0
numero = int( numero )
verifica = False
while ( verifica == False ):
    for i in numeraleAlieno:
        numero = numero + ( int(i) * int(base**potenza) )
        potenza = potenza - 1
    if ( numero == numeroTerrestre):
        print ("il numero alieno è rappresentato in base:", base)
        verifica = True
    else:
        base = base +1
        numero = 0
        potenza = len(numeraleAlieno) -1
    

    

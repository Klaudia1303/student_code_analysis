numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre="9510990939794952322311710154344301747012051743844839"


potenza = len(numeraleAlieno) - 1
ris = len(numeroTerrestre) / len(numeraleAlieno)
#print(ris)



somma = 0
resto = 0
numeroFinale = ''
numero = int(numeroTerrestre)
for i in range(2,100):
    while(numero > 0):
        resto = numero % i
        numero //= i
        numeroFinale += str(resto)
    numeroFinale = numeroFinale[::-1]
    numero = int(numeroTerrestre)
    if(numeroFinale == numeraleAlieno):
        print('La base del numero alieno è:' + str(i))
    else:
        numeroFinale = ''

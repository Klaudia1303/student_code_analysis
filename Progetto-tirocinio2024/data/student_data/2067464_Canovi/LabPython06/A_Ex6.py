numeraleAlieno = "349776123345679876543234567876543234569055"
numeroTerrestre = 9510990939794952322311710154344301747012051743844839

s = numeraleAlieno[::-1]
numDita = 1

while True:
    somma = 0
    for i in range(len(numeraleAlieno)):
        increm = (int(s[i]) * (numDita ** i))
        somma = somma + increm
    if somma >= numeroTerrestre:
        print(numDita)
        break
    else:
        numDita = numDita + 1
    

numeraleAlieno="349776123345679876543234567876543234569055" #len(numalieno) = 42
numeroTerrestre=9510990939794952322311710154344301747012051743844839
for i in range(10, numeroTerrestre): #si cerca la base che è sicuramente > 10 e minore di numTer
    x = len(numeraleAlieno)-1 #gli esponenti rimangono gli stessi
    somma = 0
    for j in range(0, len(numeraleAlieno)):
        somma=somma+int(numeraleAlieno[j])*(i**x) #normale cambio di base
        x=x-1
        if somma==numeroTerrestre:
            print(i)
            break
    
        

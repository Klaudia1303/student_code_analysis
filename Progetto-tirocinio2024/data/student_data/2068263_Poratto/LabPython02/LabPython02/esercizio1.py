Ore=int(input('inserisci le ore: '))
Min=int(input('inserisci i minuti: '))
Sec=int(input('inserisci i secondi: '))
OreInMin=Ore*60
MinInSec=(Min*60)+(OreInMin*60)
SecTot=MinInSec+Sec
print(SecTot)


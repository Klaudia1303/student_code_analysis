stringa=input("Inserisci una stringa: ")
i=0
corretto=False
while not corretto and i<len(stringa):
    if ord(stringa[i])>100:
        corretto=True
    i+=1
if i==len(stringa) and not corretto:
    print("stringa consumata e carattere non trovato")
else:
    print('Il primo carattere con codice Unicode maggiore di 100 è'+' '+stringa[i-1])
    

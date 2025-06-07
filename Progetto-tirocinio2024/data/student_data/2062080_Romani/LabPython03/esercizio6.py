s=input('Inserire stringa: ')
i=0
corretto=False
while not corretto and i<len(s):
    if ord(s[i])>100:
        corretto=True
    i+=1
if i==len(s) and not corretto:
    print("stringa consumata e carattere non trovato")
else:
    print ('Il primo carattere con codice Unicode maggiore di 100 è'+' '+s[i-1])

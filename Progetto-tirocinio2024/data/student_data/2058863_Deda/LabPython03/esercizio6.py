i=0
s=str(input('Inserisci stringa non vuota '))
corretto=False
while not corretto and (s[0:i]!=s[:]):
    y=s[i]
    z=ord(y)
    if z<=100:
        i +=1
        corretto=False
        print("Stringa consumata e carattere non trovato")
    elif z>100:
        i +=1
        print("Il primo carattere con codice Unicode maggiore di 100 è",s[i-1])
        corretto=True

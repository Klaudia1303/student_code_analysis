s='a'
i=0
somma=0

while(s!='*'):
    s=input("Inserisci un numero intero: ")
    if(s!='*'):
        s=int(s)
        if(s<0):
            somma+=s

print(somma)

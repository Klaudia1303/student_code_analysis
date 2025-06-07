n=""
somma=0
while(n!="*"):
    n=input("Inserisci un intero: ")
    if(n!="*"):
        n=int(n)
        if(n<0):
            somma+=n
print(somma)

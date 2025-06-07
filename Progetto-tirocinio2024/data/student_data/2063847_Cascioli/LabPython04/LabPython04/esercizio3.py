n=input("Inserisci un numero intero:")
i=0
while(n!='*'):
    n=input("Inserisci un numero intero:")
    if(n!='*'):
        n=int(n)
        if(n<0):
            i+=n
print("La somma dei negativi e' : ",i)

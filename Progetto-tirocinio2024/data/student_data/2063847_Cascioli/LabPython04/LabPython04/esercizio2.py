n=input("Inserisci un numero intero:")
i=0
while(n!='*'):
    n=input("Inserisci un numero intero:")
    if(n!='*'):
        n=int(n)
        if(n>0):
            i+=1
print("I numeri positivi sono",i)

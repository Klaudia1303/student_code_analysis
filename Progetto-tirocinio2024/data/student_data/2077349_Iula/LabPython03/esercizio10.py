n=int(input("Inserisci un numero intero maggiore di 1: "))
i=2
while i<=n:
    primo=True
    divisore=2
    while divisore<i:
        if i%divisore==0:
            primo=False
        divisore+=1
    if primo==True:
        print(i)
    i+=1
    




        


n=int(input("Inserisci un numero intero: "))
i=0
a=0
b=1
somma=0
while(i<n+1):
    print(a)
    somma=a+b
    a=b
    b=somma
    i+=1
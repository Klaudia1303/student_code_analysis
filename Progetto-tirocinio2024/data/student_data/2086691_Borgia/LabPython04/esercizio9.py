n=int(input("Inserire un numero intero, maggiore di 0: "))
somma=1
sommatot=1
while n!=0:
    print(somma)
    sommatot=somma+sommatot
    somma=sommatot-somma
    n-=1

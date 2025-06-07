n=int(input("Inserire un intero: "))
somma=0
while not (n==0):
    if(n%3==0):
        somma=somma+n
    n=int(input("Inserire un intero: "))
print(somma)

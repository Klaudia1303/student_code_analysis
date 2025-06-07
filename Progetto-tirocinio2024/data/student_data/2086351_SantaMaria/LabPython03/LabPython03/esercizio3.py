i=0
n=1
while i<n:
    n=int(input('Inserisci un intero(termina con un numero divisibile per 5): '))
    if n%5==0:
        print(int(n/5))
        n=0

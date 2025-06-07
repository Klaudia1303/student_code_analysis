somma=0
n=1
while n!=0:
    n=int(input('inserisci un numero intero: '))
    if n%3==0:
        somma+=n
    if n==0:
        print(somma)
        break

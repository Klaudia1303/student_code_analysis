n=int(input('Inserisci un numero intero: '))
x=0
while n!=0:
    if n%3==0:
        x=x+n
    n=int(input('Inserisci un numero intero: '))
print(x)
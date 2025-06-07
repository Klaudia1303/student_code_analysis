n=input('Inserisci un numero intero: ')
x=0
while n!='*':
    n=int(n)
    if n<0:
        x=x+n
    n=input('Inserisci un numero intero: ')
print(x)
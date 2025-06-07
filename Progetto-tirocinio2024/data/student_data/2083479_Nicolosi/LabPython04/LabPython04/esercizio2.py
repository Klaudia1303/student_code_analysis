n=input('Inserisci un numero intero: ')
x=0
while n!='*':
    n=int(n)
    if n>0:
        x+=1
    n=input('Inserisci un numero intero: ')
print(x)
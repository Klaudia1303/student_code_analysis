n1=int(input('Inserisci un numero intero positivo: '))
n2=int(input('Inserisci un altro numero intero positivo: '))
for n in range(1,n2):
    if n%n1==0:
        print(n)
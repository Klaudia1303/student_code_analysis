n1=int(input('Inserisci un numero: '))
n2=int(input('Inserisci un numero: '))

for i in range(n1, 0,-1):
    if n1%i==0 and n1%i!=n2%i:
        print(i)

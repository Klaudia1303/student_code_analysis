n1=int(input('Inserisci un numero intero: '))
n2=int(input('Inserisci un numero intero: '))
i=n1
while i!=0:
    if n1%i==0 and n2%i!=0:
        print(i)
    i-=1
n1=int(input('inserisci un numero intero: '))
n2=int(input('inserisci un numero intero: '))
for i in range(n1,1,-1):
    if n1%i==0 and n2%i!=0:
        print(i)

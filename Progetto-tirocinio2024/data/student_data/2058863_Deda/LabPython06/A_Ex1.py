n1=int(input('Inserisci intero 1 '))
n2=int(input('Inserisci intero 2 '))
for i in range(n1+1,1,-1):
    if n1%i==0 and n2%i!=0:
        print(i)

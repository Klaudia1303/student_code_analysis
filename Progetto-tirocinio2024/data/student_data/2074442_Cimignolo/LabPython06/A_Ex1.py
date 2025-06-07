n1=int(input('inserisci un numero n: '))
n2=int(input('inserisci un numero n: '))

for i in range(n1,1,-1):
    if n1%i==0:
        if n2%i!=0:
            print(i)

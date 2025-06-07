n1=int(input('inserisci un numero intero maggiore di zero: '))
n2=int(input('inserisci un numero intero maggiore di zero: '))
div=n1
for i in range(n1,-1,-1):
    if (i!=0 and n1%i==0 and n2%i!=0):
        print(i)

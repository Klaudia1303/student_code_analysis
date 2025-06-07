n1=int(input('Inserisci un intero >0 '))
n2=int(input('Inserisci un secondo intero >0 '))
for i in range(max(n1,n2),1,-1):
    if ((n1%i)==0 and (n2%i)!=0):
        print(i)

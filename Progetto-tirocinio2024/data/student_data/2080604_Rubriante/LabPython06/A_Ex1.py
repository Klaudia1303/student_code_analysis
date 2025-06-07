n1=int(input("Inserisci un numero: "))
n2=int(input("Inserisci un'altro numero: "))
for i in range(n1,1,-1):
    if n1%i==0 and n2%i!=0:
        print(i)

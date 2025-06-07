n1=int(input("inserisci un numero intero positivo: "))
n2=int(input("inserisci un'altro numero intero positivo: "))
i=n1
T=True

while T==True:
    if i<n2:
        print(i)
        i+=n1
    else:
        T=False

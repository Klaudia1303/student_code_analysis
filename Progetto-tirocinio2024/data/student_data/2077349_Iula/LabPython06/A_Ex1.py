n1=int(input("Inserisci un numero maggiore di 0: "))
n2=int(input("Inserisci un numero maggiore di 0: "))
for i in range(n1,1,-1):
    if n1%i==0:
        if n2%i==0:
            continue
        else:
            print(i)


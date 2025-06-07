n1=int(input("Inserisci intero: "))
n2=int(input("Inserisci intero: "))
for i in range(n1,0,-1):
    if n1%i==0:
        if n2%i!=0:
            print(i)

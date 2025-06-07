n1 = int(input("inserisci il primo numero: "))
n2 = int(input("inserisci il secondo numero: "))
for i in range(n1,1,-1):
    if n1%i==0 and n2%i!=0:
        print(i)

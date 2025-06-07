n=int(input("Inserisci il primo numero: "))
n2=int(input("Inserisci il secondo numero: "))
for i in range(n,n2):
    if i%n==0:
        print(i)
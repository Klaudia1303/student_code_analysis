n1=int(input("Inserisci un numero intero: "))
n2=int(input("Inserisci un numero intero: "))
massimo=0
if(n1>n2):
    massimo=n1
else:
    massimo=n2

for i in range(1, massimo+1):
    if(n1%i==0 and n2%i!=0):
        print(i)
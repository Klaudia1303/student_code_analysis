n1=int(input("Inserisci un numero intero: "))
n2=int(input("Inserisci un numero intero: "))
n3=int(input("Inserisci un numero intero: "))

if(n1>n2 and n1>n3):
    max=n1
elif(n2>n1 and n2>n3):
    max=n2
elif(n3>n1 and n3>n2):
    max=n3

if(n1<n2 and n1<n3):
    min=n1
elif(n2<n1 and n2<n3):
    min=n2
elif(n3<n1 and n3<n2):
    min=n3

if(n1<max and n1>min):
    med=n1
elif(n2<max and n2>min):
    med=n2
elif(n3<max and n3>min):
    med=n3

print("", max,"\n", med, "\n", min)
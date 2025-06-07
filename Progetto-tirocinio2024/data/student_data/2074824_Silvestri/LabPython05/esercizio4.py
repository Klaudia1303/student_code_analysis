n1=int(input("Inserisci un numero intero:"))
n2=int(input("Inserisci un numero intero:"))
x=n1
corretto=True
while corretto==True:
    if x < n2:
        print(x)
        x=x+n1
    else:
        corretto=False

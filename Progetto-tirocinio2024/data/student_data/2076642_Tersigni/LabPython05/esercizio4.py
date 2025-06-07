n1=int(input("inserisci un intero: "))
n2=int(input("inserisci un intero: "))
x=n1
corretto=True
while corretto==True:
    if x < n2:
        print(x)
        x=x+n1
    else:
        corretto=False

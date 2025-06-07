n=int(input("Inserisci un numero maggiore di zero:"))
n1=1
n2=1
while n>0:
    print(n1)
    n1+=n2
    n-=1
    if n>0:
        print(n2)
        n2+=n1
    n-=1

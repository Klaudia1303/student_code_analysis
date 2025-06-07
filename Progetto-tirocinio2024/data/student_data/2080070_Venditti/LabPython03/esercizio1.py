n=int(input("inserisci un intero maggiore di 2"))
x=2
if n>2:
    while x<=n:
        if x%2==0:
            print(x)
        x+=1
if n<=2:
    print('valore errato')

n=int(input("Inserisci lato di un quadrato: "))
if n%2!=0:
    if n>=3:
        print("*"*n)
        for i in range(1,n-1):
            print("*"+" "*(n-2)+"*")
        print("*"*n)
    else:
        print("Errore")
else:
    print("Errore")

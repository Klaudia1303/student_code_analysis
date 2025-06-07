n=int(input("Inserisci base triangolo isoscele: "))
if n%2!=0:
    if n>=3:
        spazio=n//2
        for i in range(1,n+1,2):
            print(" "*(spazio),end="")
            for j in range(i):
                print("*",end="")
            spazio=spazio-1
            print()
    else:
        print("Errore")
else:
    print("Errore")

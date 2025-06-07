n=int(input("Inserisci il lato del quadrato: "))
if n % 2 != 0 and n>=3:       
    for i in range(1,n+1):
            for j in range(1,n+1):
                if(i == 1) or (i == n) or (j == 1) or (j == n):
                    print("*", end="")
                else:
                    print(" ", end="")
            print()

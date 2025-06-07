n=int(input("Inserisci un numero intero  maggiore o uguale a due per il lato del quadrato: "))
for i in range(1,n+1):
    for c in range(1,n+1):
        if i==1 or c==1 or c==n or i==n or c==i or c+i==n+1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    


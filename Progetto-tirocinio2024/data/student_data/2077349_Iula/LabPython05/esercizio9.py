n=int(input("Inserisci un numero intero dispari maggiore o uguale a tre per il lato del quadrato: "))
print("*"*n)
for i in range(1,n-1):
    print("*"," "*(n-2),"*",sep="")
print("*"*n)

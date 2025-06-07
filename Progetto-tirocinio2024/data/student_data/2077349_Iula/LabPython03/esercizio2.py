n=int(input("Inserisci un intero maggiore di zero: "))
divisore=1
while divisore<=n:
    if n%divisore==0:
        print(divisore,"\n")
        divisore=divisore+1
    else:
        divisore=divisore+1

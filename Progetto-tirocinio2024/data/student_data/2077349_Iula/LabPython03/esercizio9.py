n=int(input("Inserisci un numero: "))
divisore=1
while divisore<=n:
    if n==1:
        print("numero primo")
        break
    elif n%divisore==0:
        if divisore!=1 and divisore!=n:
            print("numero non primo")
            break
        elif divisore==1:
            divisore=divisore+1
        elif divisore==n:
            print("numero primo")
            break
    else:
        divisore=divisore+1

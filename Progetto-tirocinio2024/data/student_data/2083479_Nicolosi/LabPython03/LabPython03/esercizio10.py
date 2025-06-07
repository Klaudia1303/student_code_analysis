n=int(input('Inserisci un numero: '))
if n==2:
    print(2)
elif n==3:
    print(2)
    print(3)
else:
    k=int(3)
    while k<=n:
        i=int(2)
        while k%1!=0 and i<k/2:
            i+=1
        if k%i!=0:
            print(k)
        k+=1
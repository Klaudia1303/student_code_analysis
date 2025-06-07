n1 = int(input("Inserisci numero n1: "))
n2 = int(input("Inserisci numero n2: "))

if n1>0 and n2>0:

    M = int(max(n1,n2))
    m = int(min(n1,n2))


    for i in range(M+1,1,-1):

        d1 = M%i

        d2 = m%i

        if d1==0 and not(d2==0):
            
            print(i)










else:
    print("Numeri non corretti")

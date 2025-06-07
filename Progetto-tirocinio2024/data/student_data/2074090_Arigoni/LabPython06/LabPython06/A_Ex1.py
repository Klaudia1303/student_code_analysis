n=int(input("Inserisci un numero >0 : "))
n1=int(input("Inserisci un numero >0 : "))
divisore=0
for i in range(n+1,2,-1):
    if n%i==0:
        divisore=i
        if n1%divisore==0:
            continue
        elif n1%divisore !=0:
           print(divisore)

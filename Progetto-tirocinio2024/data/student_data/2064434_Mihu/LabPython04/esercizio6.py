continua=True
somma=0
negativo=False
n1=int(input("Inserisci il primo numero: "))
n2=int(input("Inserisci il secondo numero: "))
if n1==0 or n2==0:
    print(somma)
    
if n1>0 and n2>0:
    while n2!=0:
        somma=somma+n1
        n2=n2-1
    print(somma)

if n1<0 and n2>0:
    while n2!=0:
        somma=somma+n1
        n2=n2-1
    print(somma)
        
if n1>0 and n2<0:
    while n2!=0:
        somma=somma-n1
        n2=n2+1
    print(somma)
        
if n1<0 and n2<0:
    while n2!=0:
        somma=somma-n1
        n2=n2+1
    print(somma)


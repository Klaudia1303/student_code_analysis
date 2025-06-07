n1=int(input('Inserire intero:'))
n2=int(input('Inserire intero:'))
contatore=0
somma=0
if n2==0 or n1==0:
    print(n2)
if n2!=0 and n1!=0:
    while contatore<n2:
        somma=somma+n1
        contatore+=1
    while n2<contatore:
        somma=somma-n1
        contatore-=1
    print(somma)
    

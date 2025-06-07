n1= int(input('numero1: '))
n2= int(input('numero2: '))
x=0
ris=0

if n2<1:
    while n2<-1:
        n2= n2+1
        x= x+n1
        ris= n1+x
        ris= -ris
    print(ris)
elif n2>1:
    while n2>1:
        n2= n2-1
        x= x+n1
        ris= n1+x
    print(ris)

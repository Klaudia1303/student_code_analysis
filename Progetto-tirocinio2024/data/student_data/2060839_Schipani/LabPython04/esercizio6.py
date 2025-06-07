import math
n1=int(input('inserisci un numero '))
n2=int(input('inserisci un numero '))
ris=0
i=1
if n1>0 and n2>0:
    while i<=n2:
        ris+=n1
        i+=1
    print(ris)
if n1<0 and n2<0:
    while i<=abs(n2):
        ris+=abs(n1)
        i+=1
    print(ris)
if n1<0 and n2>0:
    while i<=n2:
        ris-=abs(n1)
        i+=1
    print(ris)
if n1>0 and n2<0:
    while i<=abs(n2):
        ris-=n1
        i+=1
    print(ris)
if n1==0 or n2==0:
    print('0')
       


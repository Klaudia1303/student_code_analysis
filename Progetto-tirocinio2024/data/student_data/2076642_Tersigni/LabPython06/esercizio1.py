n1=int(input("inserisci un intero >0: "))
n2=int(input("inserisci un intero >0: "))
if n1>=n2:
    i=n1
else:
    i=n2
while i!=0:
    if n1%i==0 and n2%i!=0:
        print(i)
    i-=1
    

n1=int(input('inserisci un intero positivo:'))
n2=int(input('inserisci un intero positivo:'))
m=1
for m in range(n1,n2):
    if m%n1==0:
        print(m)
        m+=1

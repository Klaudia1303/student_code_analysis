n1=int(input('inserisci un intero: '))
n2=int(input('inserisci un intero: '))
for c in reversed(range(1,n1+1)):
    if n2%c==0:
        continue
    if n1%c==0:
        print(c)
    

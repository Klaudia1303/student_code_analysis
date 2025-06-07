n=int(input('Inserisci un numero intero: '))
while n>1:
    i=1
    m=0
    while i<=n:
        if n%i==0:
            m+=1
        i+=1
    if m<3 and n!=0:
        print(n)
    n-=1 #in questo modo ogni volta diminuisce di una unità n e di analizzano
         #tutti i numeri fino a 2, n=1 no perchè non soddisfa la condizione per
         #entrare nel ciclo
        

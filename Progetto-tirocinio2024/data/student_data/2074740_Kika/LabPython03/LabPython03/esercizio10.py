numero=int(input('inserisci un intero maggiore di 1: '))
i=2
while i<=numero:
    div=2
    while (i%div!=0 and div<i):
        div=div+1
    if div==i:
        print(i)
    i=i+1
        
        

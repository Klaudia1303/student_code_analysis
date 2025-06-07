n=int(input("Inserisci un numero intero maggiore di 1: "))
i=2
while i<=n:
    x=i-1
    primo=1
    while x>1:
        if i%x==0:
            primo=0
        x-=1
    if primo==1:
        print(i)
    i+=1

n=int(input("Inserisci numero intero maggiore di 1 "))
while n<=1:
    if n<=1:
        n=int(input("Inserisci un intero maggiore di 1! "))

i=2
while i!=n+1:
    x=1
    y=0
    while x!=i+1:
        if i%x==0:
            y+=1
        x+=1
    if y==2:
        print(i)
    i+=1

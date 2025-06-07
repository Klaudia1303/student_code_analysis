n=int(input('Inserisci intero maggiore di 1: '))
i=2
count=0
j=2
while j<=n:
    while i<=j/2 and count==0:
        if j%i==0:
            count+=1
        i+=1
    if count==0:
        print(j)
    i=2
    count=0
    j+=1

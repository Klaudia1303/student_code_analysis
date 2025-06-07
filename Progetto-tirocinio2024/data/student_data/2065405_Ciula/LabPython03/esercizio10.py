n=int(input("Inserisci un numero maggiore di 1: "))
i=2
while(i<=n):
    c=0
    j=2
    while(j<i):
        if(i%j==0):
            c+=1
            j+=1
        else:
            j+=1
    if(c==0):
        print(i)
    i+=1
